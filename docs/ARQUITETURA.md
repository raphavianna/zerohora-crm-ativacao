# Arquitetura — ativação de CRM

## Objetivo

Ativar a base de clientes (email + WhatsApp) a partir dos segmentos definidos no
painel, com contato real, consentimento e log auditável — **isolando a PII** do
dashboard.

Princípio: **o painel define o QUEM (zero-PII), este repo faz o ENVIAR (com PII)**.
A junção acontece pelo `id_cliente` pseudônimo, reproduzido de forma idêntica aos
dois lados.

## Dois artefatos de fronteira

1. **Audience spec** (painel → aqui): `zerohora.audience-spec/v1`. Regra do segmento
   + lista de `id_cliente` pseudônimos + atributos não-PII + intenção/canal. É o
   gatilho de uma campanha. Contrato: `docs/CONTRATO-AUDIENCE-SPEC.md`.
2. **Mapa de cobertura** (aqui → painel): `zerohora.contatos-cobertura/v1`. Booleans
   por `id_cliente` (tem email/whatsapp + consentimento). Deixa o painel mostrar
   "ativáveis". Contrato: `docs/CONTRATO-CONTATOS-COBERTURA.md`.

## Fluxo de uma campanha

```
1. Painel  → exporta audience-spec-<intencao>.json (IDs pseudônimos)
2. Aqui    → resolve id_cliente → contato via de-para (PII, local/seguro)
3. Aqui    → filtra por consentimento/opt-out/suppression do canal
4. Aqui    → renderiza a mensagem (skill zerohora-crm-copywriter) usando os atributos
5. Aqui    → dispara (email / WhatsApp) respeitando rate-limit e templates aprovados
6. Aqui    → grava log de envio + resultado (auditável)
7. Aqui    → regenera contatos_cobertura.json e publica ao painel
```

## De-para id_cliente → contato

`id_cliente = "c" + sha1((user_login || email || dígitos(phone)).lower())[:10]`
(idêntico a `capturar_vendas_baselinker.py` do painel). A de-para é construída a
partir de Baselinker (getOrders) + Nuvemshop, guardada **fora do git**. Só booleans
derivados dela viram o mapa de cobertura.

## Disparo (a definir)

- **Email:** provedor a definir (Resend / SendGrid / SES). Domínio próprio com
  DKIM/SPF, templates, tracking de entrega/abertura.
- **WhatsApp:** provedor a definir (Meta Cloud API direto ou BSP). Exige templates
  aprovados e número business; respeitar janelas e limites de envio.

## Segurança / LGPD

- PII nunca versionada (`.gitignore`).
- Consentimento por canal é pré-condição de envio; opt-out/suppression sempre vencem.
- Log de envio auditável (quem, quando, qual template, resultado) — sem expor o
  conteúdo de contato além do necessário.
