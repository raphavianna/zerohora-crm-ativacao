# cobertura — mapa de contato (booleans) para o painel

`gerar_cobertura.mjs` lê um arquivo de contatos e emite `contatos_cobertura.json`
(schema `zerohora.contatos-cobertura/v1`) — só booleans por `id_cliente`, zero-PII.

## Entrada (`--in`, JSON array)

Cada registro traz a identidade do cliente (a mesma do painel) + contato/consent:

```jsonc
[
  { "user_login": "surfista_jc", "email": "jc@x.com", "phone": "+55 48 99999-1111",
    "optin_email": true, "optin_whatsapp": true }
]
```

- `id_cliente` é derivado como no painel: `chave = user_login || email || dígitos(phone)`
  (minúscula/trim); `id_cliente = "c" + sha1(chave)[:10]`. **Paridade verificada.**
- `email`/`whatsapp` no mapa = existe contato válido no canal.
- `consent_*` = há opt-in **e** não está em suppression. Por padrão, sem `optin_*`
  explícito o consentimento é **false** (LGPD). `--assume-consent email,whatsapp`
  liga um default (decisão explícita do operador).

## Rodar

```bash
npm run cobertura -- --in exports/contatos.json --out contatos_cobertura.json \
  --suppress contatos/suppression.json --fonte baselinker+nuvemshop
# teste com dados fictícios:
npm run cobertura:exemplo
```

## Publicar ao painel

O `contatos_cobertura.json` gerado vai para `public/data/contatos_cobertura.json` do
`zerohora-painel` (processo controlado — commit/deploy). O painel acende o KPI
"Ativáveis" e o filtro "Só ativáveis" automaticamente.

> O arquivo de entrada (`exports/contatos.json`) e a de-para são **PII** e ficam
> fora do git. Só o mapa de booleans sai daqui.
