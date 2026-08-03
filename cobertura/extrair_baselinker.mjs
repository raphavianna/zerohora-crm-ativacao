#!/usr/bin/env node
// Baselinker (getOrders) -> contatos_cobertura.json (booleans por id_cliente).
// Baselinker é a fonte de vendas GERAL (marketplaces + site via Nuvemshop), então
// cobre a maior parte dos contatos. Lê email/telefone só EM MEMÓRIA; nada de PII
// persiste — só os booleans saem. Mesmo id_cliente do painel (paridade verificada).
//
// Env:  BASELINKER_API_TOKEN
// Uso:
//   node cobertura/extrair_baselinker.mjs --desde 2026-01-01 --out contatos_cobertura.json \
//        [--assume-consent email,whatsapp] [--suppress contatos/suppression.json] [--mock exports/orders.exemplo.json]
//
// Consentimento: o Baselinker NÃO traz opt-in de marketing. Sem uma fonte de opt-in,
// consent_* fica false (LGPD). --assume-consent liga um default explícito por canal
// (decisão do operador); suppression sempre vence.

import { readFileSync, writeFileSync } from 'node:fs'
import { acumula, carregarSuppression, resumo, envelope } from './lib.mjs'

const API = 'https://api.baselinker.com/connector.php'
const args = Object.fromEntries(
  process.argv.slice(2).reduce((a, v, i, arr) => (v.startsWith('--') ? [...a, [v.slice(2), arr[i + 1]?.startsWith('--') ? true : arr[i + 1]]] : a), [])
)
const OUT = args.out || 'contatos_cobertura.json'
const DESDE = args.desde || '2026-01-01'
const assume = new Set(String(args['assume-consent'] || '').split(',').map((s) => s.trim()).filter(Boolean))
const supp = carregarSuppression(readFileSync, args.suppress === true ? null : args.suppress)
const desdeUnix = Math.floor(Date.parse(`${DESDE}T00:00:00-03:00`) / 1000)

async function call(token, method, params = {}) {
  const body = new URLSearchParams({ method, parameters: JSON.stringify(params) })
  const r = await fetch(API, { method: 'POST', headers: { 'X-BLToken': token }, body })
  if (!r.ok) throw new Error(`${method} HTTP ${r.status}`)
  const j = await r.json()
  if (j.status !== 'SUCCESS') throw new Error(`${method} falhou: ${JSON.stringify(j).slice(0, 200)}`)
  return j
}

// Pagina getOrders por date_confirmed (100/página, respeitando 100 req/min).
async function* iterOrders(token, desde) {
  let frm = desde
  const vistos = new Set()
  for (;;) {
    const j = await call(token, 'getOrders', { date_confirmed_from: frm, get_unconfirmed_orders: false })
    const orders = j.orders || []
    const novos = orders.filter((o) => !vistos.has(o.order_id))
    if (!novos.length) break
    for (const o of novos) { vistos.add(o.order_id); yield o }
    if (orders.length < 100) break
    frm = Number(orders[orders.length - 1].date_confirmed)
    await new Promise((res) => setTimeout(res, 400))
  }
}

// Transforma um iterável de orders no mapa de cobertura (testável sem rede).
export function coberturaDeOrders(orders, { assume, supp }) {
  const cobertura = {}
  let n = 0, semChave = 0
  for (const o of orders) { n++; if (!acumula(cobertura, o, { assume, supp })) semChave++ }
  return { cobertura, n, semChave }
}

async function main() {
  let orders
  if (args.mock && args.mock !== true) {
    orders = JSON.parse(readFileSync(args.mock, 'utf8'))
    console.log(`[mock] ${orders.length} orders de ${args.mock}`)
  } else {
    const token = (process.env.BASELINKER_API_TOKEN || '').trim()
    if (!token) { console.error('ERRO: BASELINKER_API_TOKEN não definido (ou use --mock).'); process.exit(1) }
    orders = []
    for await (const o of iterOrders(token, desdeUnix)) orders.push(o)
    console.log(`[baselinker] ${orders.length} pedidos desde ${DESDE}`)
  }

  const { cobertura, n, semChave } = coberturaDeOrders(orders, { assume, supp })
  writeFileSync(OUT, JSON.stringify(envelope(cobertura, 'baselinker', new Date().toISOString())))
  const s = resumo(cobertura)
  console.log(`[cobertura] ${s.ids} id_cliente de ${n} pedidos · email ${s.email} (consent ${s.consentEmail}) · ` +
    `whatsapp ${s.whatsapp} (consent ${s.consentWhatsapp}) · ${semChave} sem chave`)
  console.log(`gravado: ${OUT}`)
}

main().catch((e) => { console.error(e.message); process.exit(1) })
