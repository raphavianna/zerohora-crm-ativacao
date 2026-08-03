# ativacao — disparo email / WhatsApp (a definir)

Consome a **audience spec** do painel, resolve contato (de-para), filtra por
consentimento e dispara. Provedores **a definir** — a estrutura fica pronta e
plugável.

## Fluxo

1. Ler `audience-spec-*.json` (schema `zerohora.audience-spec/v1`).
2. Resolver `id_cliente → contato` (de-para em `contatos/`, PII).
3. Filtrar por `canal_sugerido` + consentimento/opt-out/suppression.
4. Renderizar a mensagem (skill `zerohora-crm-copywriter`) com `intencao` + atributos
   não-PII do segmento (`categoria_preferida`, `recencia_dias`, ...).
5. Disparar com rate-limit e templates aprovados.
6. Gravar log auditável (id_cliente, canal, template, timestamp, resultado).

## Provedores (decidir)

- **Email:** Resend / SendGrid / Amazon SES. Domínio próprio (DKIM/SPF), templates.
- **WhatsApp:** Meta Cloud API (direto) ou BSP (Twilio / 360dialog). Templates
  aprovados + número business + limites de envio.

## Ainda não implementado

Este diretório é um placeholder da Etapa 4. O disparo real entra quando os
provedores forem escolhidos; nada aqui envia mensagem ainda.
