// Helpers compartilhados da cobertura. id_cliente reproduzido EXATAMENTE como no
// painel (capturar_vendas_baselinker.py): chave = user_login || email ||
// só-dígitos(phone), minúscula/trim; id = "c" + sha1(chave)[:10].
import { createHash } from 'node:crypto'

export const digits = (s) => String(s || '').replace(/\D/g, '')
export const emailValido = (s) => /.+@.+\..+/.test(String(s || '').trim())
export const phoneValido = (s) => digits(s).length >= 10 // celular BR com DDD

export function chaveCliente(o) {
  for (const f of ['user_login', 'email']) {
    const v = (o[f] || '').trim().toLowerCase()
    if (v) return v
  }
  return digits(o.phone)
}
export const idCliente = (chave) => (chave ? 'c' + createHash('sha1').update(chave).digest('hex').slice(0, 10) : '')

export function carregarSuppression(readFileSync, path) {
  if (!path) return { email: new Set(), phone: new Set() }
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

// Acumula um registro (order/contato) no mapa de cobertura. Retorna false se sem chave.
// PII (email/phone) é lido só em memória; nada além dos booleans persiste.
export function acumula(cobertura, o, { assume, supp }) {
  const id = idCliente(chaveCliente(o))
  if (!id) return false
  const temEmail = emailValido(o.email)
  const temPhone = phoneValido(o.phone)
  const emailSup = temEmail && supp.email.has(String(o.email).trim().toLowerCase())
  const phoneSup = temPhone && supp.phone.has(digits(o.phone))
  const optinEmail = o.optin_email === true || (assume.has('email') && o.optin_email !== false)
  const optinWhats = o.optin_whatsapp === true || (assume.has('whatsapp') && o.optin_whatsapp !== false)
  const a = cobertura[id] || { email: false, whatsapp: false, consent_email: false, consent_whatsapp: false }
  cobertura[id] = {
    email: a.email || temEmail,
    whatsapp: a.whatsapp || temPhone,
    consent_email: a.consent_email || (temEmail && optinEmail && !emailSup),
    consent_whatsapp: a.consent_whatsapp || (temPhone && optinWhats && !phoneSup),
  }
  return true
}

export function resumo(cobertura) {
  const ids = Object.values(cobertura)
  const c = (f) => ids.filter((x) => x[f]).length
  return { ids: ids.length, email: c('email'), consentEmail: c('consent_email'), whatsapp: c('whatsapp'), consentWhatsapp: c('consent_whatsapp') }
}

export function envelope(cobertura, fonte, nowISO) {
  return { schema: 'zerohora.contatos-cobertura/v1', gerado_em: nowISO, fonte, cobertura }
}
