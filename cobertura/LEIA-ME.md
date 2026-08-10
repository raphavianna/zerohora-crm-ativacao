# cobertura — mapa de contato (booleans) para o painel

Gera `contatos_cobertura.json` (schema `zerohora.contatos-cobertura/v1`) — só booleans
por `id_cliente`, zero-PII. Duas entradas, mesma saída:

- **`extrair_baselinker.mjs`** (principal): puxa contato do Baselinker (getOrders),
  a fonte de vendas GERAL (marketplaces + site via Nuvemshop). É o caminho de
  produção.
- **`gerar_cobertura.mjs`** (genérico): recebe um JSON array de contatos já pronto
  (ex.: export de outra fonte).

`lib.mjs` concentra o `id_cliente` (idêntico ao painel: `chave = user_login || email
|| dígitos(phone)`, minúscula/trim; `id = "c" + sha1(chave)[:10]` — **paridade
verificada**) e a regra de consentimento.

## Rodar

```bash
# Baselinker (produção) — precisa de BASELINKER_API_TOKEN:
BASELINKER_API_TOKEN=xxx node cobertura/extrair_baselinker.mjs --desde 2026-01-01 --out contatos_cobertura.json

# teste sem rede (dados fictícios):
npm run cobertura:exemplo

# fonte genérica (JSON array pronto):
node cobertura/gerar_cobertura.mjs --in exports/contatos.json --fonte nuvemshop
```

## Consentimento (LGPD)

O Baselinker **não** traz opt-in de marketing. Sem uma fonte de opt-in, `consent_*`
fica **false**. `--assume-consent email,whatsapp` liga um default explícito por canal
(decisão do operador). `--suppress contatos/suppression.json` (opt-outs) sempre vence.
Quando houver uma base de opt-in real, ela entra aqui como fonte de consentimento.

## Publicar ao painel

O workflow `.github/workflows/cobertura.yml` roda a extração e:
1. sobe o `contatos_cobertura.json` como **artifact** (só booleans), e
2. se o secret `PAINEL_PUSH_TOKEN` (write no painel) existir, commita direto em
   `public/data/contatos_cobertura.json` do `zerohora-painel`.

Sem o token, baixe o artifact e commite manualmente no painel. Assim que o arquivo
chega ao painel, o KPI "Ativáveis" e o filtro "Só ativáveis" acendem sozinhos.

> `exports/` e `contatos/` são PII e ficam fora do git. Só o mapa de booleans sai.
