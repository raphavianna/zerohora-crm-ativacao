#!/usr/bin/env node
// Gera o mapa de cobertura (contatos_cobertura.json) a partir de um arquivo de
// contatos genérico (JSON array). Para a fonte Baselinker, use extrair_baselinker.mjs.
// Sem PII na saída: só booleans por id_cliente (ver docs/CONTRATO-CONTATOS-COBERTURA.md).
//
// Entrada (--in, JSON array): { user_login?, email?, phone?, optin_email?, optin_whatsapp? }
// Uso:
//   node cobertura/gerar_cobertura.mjs --in exports/contatos.json --out contatos_cobertura.json \
//        [--suppress contatos/suppression.json] [--assume-consent email,whatsapp] [--fonte nuvemshop]

import { readFileSync, writeFileSync } from 'node:fs'
import { acumula, carregarSuppression, resumo, envelope } from './lib.mjs'

const args = Object.fromEntries(
  process.argv.slice(2).reduce((a, v, i, arr) => (v.startsWith('--') ? [...a, [v.slice(2), arr[i + 1]?.startsWith('--') ? true : arr[i + 1]]] : a), [])
)
const IN = args.in || 'exports/contatos.json'
const OUT = args.out || 'contatos_cobertura.json'
const FONTE = args.fonte || 'contatos'
const assume = new Set(String(args['assume-consent'] || '').split(',').map((s) => s.trim()).filter(Boolean))
const supp = carregarSuppression(readFileSync, args.suppress === true ? null : args.suppress)

const registros = JSON.parse(readFileSync(IN, 'utf8'))
if (!Array.isArray(registros)) throw new Error('entrada deve ser um array JSON de contatos')

const cobertura = {}
let semChave = 0
for (const r of registros) if (!acumula(cobertura, r, { assume, supp })) semChave++

writeFileSync(OUT, JSON.stringify(envelope(cobertura, FONTE, new Date().toISOString())))
const s = resumo(cobertura)
console.log(`[cobertura] ${s.ids} id_cliente · email ${s.email} (consent ${s.consentEmail}) · ` +
  `whatsapp ${s.whatsapp} (consent ${s.consentWhatsapp}) · ${semChave} sem chave`)
console.log(`gravado: ${OUT}`)
