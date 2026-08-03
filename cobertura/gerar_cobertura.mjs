#!/usr/bin/env node
// Gera o mapa de cobertura de contato (contatos_cobertura.json) que o PAINEL consome
// para distinguir "identificável" de "ativável" — SEM PII (só booleans por id_cliente).
//
// Entrada: um arquivo de contatos (JSON array) com, por registro, a mesma identidade
// que o painel usa para o id_cliente + os campos de contato/consentimento:
//   { "user_login"?, "email"?, "phone"?, "optin_email"?, "optin_whatsapp"? }
//
// id_cliente é reproduzido EXATAMENTE como no pipeline do painel
// (capturar_vendas_baselinker.py): chave = (user_login || email || só-dígitos(phone)),
// minúscula/trim; id_cliente = "c" + sha1(chave)[:10]. Assim a chave casa 1:1 com o
// vendas.json. A chave crua e os contatos NUNCA saem — só os booleans.
//
// Uso:
//   node cobertura/gerar_cobertura.mjs --in exports/contatos.json --out contatos_cobertura.json \
//        [--suppress contatos/suppression.json] [--assume-consent email,whatsapp] [--fonte baselinker+nuvemshop]
//
// LGPD: por padrão consent_* = false a menos que o registro traga optin_* true (ou o
// canal esteja em --assume-consent, uma decisão explícita do operador). Suppression
// (opt-out) sempre zera o consentimento do canal.

import { readFileSync, writeFileSync } from 'node:fs'
import { createHash } from 'node:crypto'

const args = Object.fromEntries(
  process.argv.slice(2).reduce((a, v, i, arr) => (v.startsWith('--') ? [...a, [v.slice(2), arr[i + 1]?.startsWith('--') ? true : arr[i + 1]]] : a), [])
)
const IN = args.in || 'exports/contatos.json'
const OUT = args.out || 'contatos_cobertura.json'
const FONTE = args.fonte || 'baselinker+nuvemshop'
const ASSUME = new Set(String(args['assume-consent'] || '').split(',').map((s) => s.trim()).filter(Boolean))

const digits = (s) => String(s || '').replace(/\D/g, '')
const emailValido = (s) => /.+@.+\..+/.test(String(s || '').trim())
const phoneValido = (s) => digits(s).length >= 10 // celular BR com DDD

// Idêntico ao painel: chave estável do cliente, minúscula/trim, com fallback por canal.
function chaveCliente(o) {
  for (const f of ['user_login', 'email']) {
    const v = (o[f] || '').trim().toLowerCase()
    if (v) return v
  }
  return digits(o.phone)
}
const idCliente = (chave) => (chave ? 'c' + createHash('sha1').update(chave).digest('hex').slice(0, 10) : '')

function carregarSuppression(path) {
  if (!path || path === true) return { email: new Set(), phone: new Set() }
  try {
    const s = JSON.parse(readFileSync(path, 'utf8'))
    return {
      email: new Set((s.email || []).map((e) => String(e).trim().toLowerCase())),
      phone: new Set((s.phone || []).map((p) => digits(p))),
    }
  } catch (e) {
    console.error(`aviso: suppression não lido (${e.message}) — seguindo sem opt-out.`)
    return { email: new Set(), phone: new Set() }
  }
}

function main() {
  const registros = JSON.parse(readFileSync(IN, 'utf8'))
  if (!Array.isArray(registros)) throw new Error('entrada deve ser um array JSON de contatos')
  const supp = carregarSuppression(args.suppress)

  const cobertura = {}
  let semChave = 0
  for (const r of registros) {
    const chave = chaveCliente(r)
    const id = idCliente(chave)
    if (!id) { semChave++; continue }

    const temEmail = emailValido(r.email)
    const temPhone = phoneValido(r.phone)
    const emailSupresso = temEmail && supp.email.has(String(r.email).trim().toLowerCase())
    const phoneSupresso = temPhone && supp.phone.has(digits(r.phone))

    const optinEmail = r.optin_email === true || (ASSUME.has('email') && r.optin_email !== false)
    const optinWhats = r.optin_whatsapp === true || (ASSUME.has('whatsapp') && r.optin_whatsapp !== false)

    const atual = cobertura[id] || { email: false, whatsapp: false, consent_email: false, consent_whatsapp: false }
    cobertura[id] = {
      email: atual.email || temEmail,
      whatsapp: atual.whatsapp || temPhone,
      consent_email: atual.consent_email || (temEmail && optinEmail && !emailSupresso),
      consent_whatsapp: atual.consent_whatsapp || (temPhone && optinWhats && !phoneSupresso),
    }
  }

  const saida = {
    schema: 'zerohora.contatos-cobertura/v1',
    gerado_em: new Date().toISOString(),
    fonte: FONTE,
    cobertura,
  }
  writeFileSync(OUT, JSON.stringify(saida))

  const ids = Object.values(cobertura)
  const c = (f) => ids.filter((x) => x[f]).length
  console.log(`[cobertura] ${ids.length} id_cliente · email ${c('email')} (consent ${c('consent_email')}) · ` +
    `whatsapp ${c('whatsapp')} (consent ${c('consent_whatsapp')}) · ${semChave} registros sem chave`)
  console.log(`gravado: ${OUT}`)
}

main()
