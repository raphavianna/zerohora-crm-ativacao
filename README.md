# zerohora-crm-ativacao

Camada de **ativação de CRM** da Use Zero Hora: transforma os segmentos definidos no
painel (`zerohora-painel`) em **disparos de email e WhatsApp**, com contato real,
consentimento e log auditável.

É o par com-PII do painel (que é zero-PII). O painel define o **quem** (segmento +
`id_cliente` pseudônimo); este repo resolve o **como/enviar**.

## Fronteira de dados

```
PAINEL (zero-PII)                          ESTE REPO (com PII, isolado)
─────────────────                          ───────────────────────────
audience spec  ───────────────────────▶    resolve id_cliente → contato (de-para PII)
(regra + id_cliente pseudônimo)            aplica consentimento / opt-out / suppression
                                           renderiza copy (skill zerohora-crm-copywriter)
contatos_cobertura.json  ◀─────────────    dispara email + WhatsApp, grava log
(booleans, zero-PII)                       gera o mapa de cobertura (booleans) p/ o painel
```

Regra de ouro: **nada de PII versionado**. Contatos, de-para e exports crus ficam
fora do git (ver `.gitignore`). Só sai deste repo, para o painel, o
`contatos_cobertura.json` — booleans por `id_cliente`.

## Estrutura

```
zerohora-crm-ativacao/
├── cobertura/         # gera contatos_cobertura.json (booleans) para o painel
│   └── gerar_cobertura.mjs
├── contatos/          # de-para id_cliente ↔ contato (PII, gitignored)
├── exports/           # exports crus de Baselinker/Nuvemshop (PII, gitignored)
├── ativacao/          # disparo email/WhatsApp (provedores a definir)
└── docs/              # arquitetura + contratos de dados
```

## Etapas

1. **[ATUAL] Cobertura** — `id_cliente → {email,whatsapp,consent}` (booleans) para o
   painel distinguir identificável × ativável. Gerador pronto e com paridade de
   `id_cliente` verificada contra o pipeline do painel.
2. **De-para** — resolução `id_cliente → contato` a partir de Baselinker + Nuvemshop
   (PII, nunca versionada).
3. **Consentimento** — opt-in / opt-out / suppression por canal (LGPD).
4. **Disparo** — integrações de email e WhatsApp (provedores a definir) + templates.
5. **Log** — registro auditável de envio e resultado.

## id_cliente (chave de junção)

Reproduzido EXATAMENTE como no painel:
`chave = (user_login || email || só-dígitos(phone))` em minúscula/trim;
`id_cliente = "c" + sha1(chave)[:10]`. Paridade Node↔Python verificada.
