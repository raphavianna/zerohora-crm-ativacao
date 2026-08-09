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

## Segmentação por sexo — `inferir_genero.py`

Nem o painel nem o export trazem coluna de sexo. Quando a campanha precisa de um
recorte masculino/feminino (ex.: linha de sunga vs. biquíni), o único sinal
disponível é o **primeiro nome**. `inferir_genero.py` infere o sexo pelo nome
(dicionário curado PT-BR + regras morfológicas), aplica o consentimento de
marketing e monta a base de email já filtrada.

```bash
# export cru costuma vir em ISO-8859-1 (Nuvemshop); converta primeiro:
iconv -f WINDOWS-1252 -t UTF-8 exports/clientes.csv > exports/clientes.utf8.csv

# base masculina, só quem tem opt-in de marketing (Marketing == "Aceita"):
python3 ativacao/inferir_genero.py --in exports/clientes.utf8.csv --sexo M \
        --out exports/base_email_masculina.csv

# inspecionar a classificação (nada é gravado):
python3 ativacao/inferir_genero.py --in exports/clientes.utf8.csv --auditar
```

- Nomes ambíguos/desconhecidos caem em `U` e **ficam fora** da base — a escolha é por
  **precisão** (numa base "só homens", incluir uma mulher é pior que perder um homem).
- `--sem-consentimento` ignora o filtro de opt-in — **não usar para disparo** (LGPD).
- Saída tem nome + email = **PII**: vive em `exports/` (gitignored), nunca versionar.
  A ferramenta só carrega dicionários de nomes genéricos — nenhum dado de cliente.

## Ainda não implementado

Este diretório é um placeholder da Etapa 4. O disparo real entra quando os
provedores forem escolhidos; nada aqui envia mensagem ainda.
