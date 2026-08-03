# contatos — de-para id_cliente ↔ contato (PII)

**Conteúdo desta pasta é PII e NÃO é versionado** (ver `.gitignore`). Aqui vive a
resolução `id_cliente → {email, telefone, nome, ...}` construída a partir de
Baselinker (getOrders) + Nuvemshop, além da lista de **suppression** (opt-outs).

Formato sugerido da suppression (`contatos/suppression.json`), consumido pelo gerador:

```json
{ "email": ["optout@exemplo.com"], "phone": ["5548999990000"] }
```

Nada daqui sai do repo. Só os **booleans** derivados (via `cobertura/`) chegam ao
painel.
