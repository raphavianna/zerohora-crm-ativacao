# Contrato — Audience Spec (`zerohora.audience-spec/v1`)

Artefato de handoff entre o **painel** (define o *quem*, zero-PII) e o repo de
**ativação** `zerohora-crm-ativacao` (resolve contato, aplica consentimento e
dispara email/WhatsApp). Gerado na aba **Clientes → Ativação** por download.

Regra de ouro: **o painel nunca vê contato**. A spec carrega só `id_cliente`
pseudônimo + atributos não-PII. O join `id_cliente → email/telefone` acontece só
no repo de ativação, em ambiente controlado.

## Formato

```jsonc
{
  "schema": "zerohora.audience-spec/v1",
  "gerado_em": "2026-08-03T18:00:00.000Z",
  "fonte": "zerohora-painel/clientes",
  "ancora_recencia": "2026-08-01",      // último dia da base; recência é medida contra ele
  "canal_sugerido": "email",            // "email" | "whatsapp" | "ambos"
  "intencao": "reativacao",             // reativacao | recompra | upsell | boas_vindas | vip | pesquisa
  "regra": {
    "descricao": "recorrentes · alto valor (LTV ≥ R$ 179,99) · inativos (>90d)",
    "criterios": {
      "tipo": "recorrentes",            // todos | novos | recorrentes
      "valor": "alto",                  // todos | alto (topo 25% de LTV)
      "ltv_min": null,                  // número ou null
      "recencia": "inativos",           // todos | ativos(<=30d) | risco(31-90d) | inativos(>90d)
      "canais": ["Mercado Livre"],      // canal_familia preferido; [] = todos
      "categorias": ["MAIO"]            // categoria preferida; [] = todas
    }
  },
  "resumo": { "clientes": 312, "ltv_medio": 240.5, "ticket_medio": 118.9, "receita_total": 75036.0 },
  "audiencia": [
    {
      "id_cliente": "c9e3538ed7f",      // pseudônimo (chave de join no repo de ativação)
      "ltv": 3600.0,
      "pedidos": 1,
      "recencia_dias": 128,
      "canal_preferido": "Mercado Livre",
      "categoria_preferida": "MAIO"
    }
    // ...
  ]
}
```

## Consumo no repo de ativação (esperado)

1. Resolve `id_cliente → contato` (tabela de-para com PII, fora do painel).
2. Aplica **consentimento / opt-out / suppression** por canal antes de enfileirar.
3. Renderiza a mensagem (skill `zerohora-crm-copywriter`) usando `intencao` +
   atributos (`categoria_preferida`, `recencia_dias`, etc.) para personalizar.
4. Dispara por `canal_sugerido` e grava **log de envio** auditável.

## Versionamento

`schema` fixa a versão. Mudança incompatível → `v2`. Campos novos opcionais podem
entrar em `v1` sem quebrar consumidores.
