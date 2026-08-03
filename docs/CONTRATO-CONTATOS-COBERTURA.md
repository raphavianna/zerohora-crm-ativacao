# Contrato — Mapa de cobertura de contato (`zerohora.contatos-cobertura/v1`)

Arquivo `public/data/contatos_cobertura.json`. Diz, por `id_cliente`, se há contato
e consentimento em cada canal — **sem PII**. É o que separa **identificável** (tem
`id_cliente`) de **ativável** (dá pra falar com ele).

> **Ativável = identificável ∧ tem contato ∧ consentimento ∧ não-suprimido**, por canal.

## Quem produz

O **lado de contato/ativação** (ambiente com PII), a partir de **Baselinker** (fonte
de vendas geral) + **Nuvemshop** (site próprio) + CRM. Ele resolve o contato real,
checa consentimento/opt-out, e publica de volta **só os booleans** — o painel nunca
vê email/telefone.

Regra de ouro: nenhum contato entra neste arquivo. Se um dia entrar um email/telefone,
o contrato foi violado.

## Formato

```jsonc
{
  "schema": "zerohora.contatos-cobertura/v1",
  "gerado_em": "2026-08-03T18:00:00.000Z",
  "fonte": "baselinker+nuvemshop",
  "cobertura": {
    "c9e3538ed7f": { "email": true,  "whatsapp": true,  "consent_email": true,  "consent_whatsapp": false },
    "c5d74883f4f": { "email": false, "whatsapp": true,  "consent_email": false, "consent_whatsapp": true  }
    // ... uma entrada por id_cliente com contato conhecido
  }
}
```

- Chave = `id_cliente` (mesmo pseudônimo do `vendas.json`).
- `email` / `whatsapp` = existe contato válido nesse canal.
- `consent_email` / `consent_whatsapp` = há opt-in e não está suprimido nesse canal.
- `id_cliente` **ausente** do mapa = tratado como **não ativável** (sem contato conhecido).

## Como o painel usa

- KPI **Ativáveis (contato)** na aba Clientes: quantos dos identificáveis são
  alcançáveis por email / WhatsApp.
- Filtro **Só ativáveis** no construtor de segmento (pelo canal do disparo).
- A **audience spec** carrega `ativavel_email` / `ativavel_whatsapp` por `id_cliente`
  (ou `null` quando o mapa não está publicado).
- **Ausência do arquivo** (HTTP 404) é tolerada: o painel mostra "aguardando
  contatos_cobertura.json" e segue com identificáveis.

## Nota de negócio

Marketplace (Mercado Livre / Shopee / Shein) costuma **não** entregar o email do
comprador ao vendedor — então clientes marketplace-only tendem a ter `email:false`.
Site próprio (Nuvemshop) captura contato. Logo o `canal_preferido` do cliente já é
um bom indicador prévio de cobertura por email.
