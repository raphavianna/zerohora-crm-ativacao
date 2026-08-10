# Hospedagem das imagens do email

**Decisão: GitHub raw, com URL fixada em commit SHA.** O repositório
`raphavianna/zerohora-crm-ativacao` é público, e o raw responde 200 sem autenticação,
com `Content-Type: image/jpeg`. Testado em 10/08/2026.

---

## O que uma imagem de email precisa

| Requisito | Por quê |
|---|---|
| URL pública, sem login e sem cookie | O cliente de email busca a imagem como um visitante anônimo. Qualquer autenticação vira imagem quebrada |
| HTTPS | Cliente moderno bloqueia conteúdo misto |
| `Content-Type` de imagem correto | Servido como `text/plain`, o cliente não renderiza |
| **URL permanente** | Um email fica anos na caixa de entrada de quem recebeu. A URL precisa sobreviver a tudo que acontecer no repositório depois do disparo |
| Resposta rápida e estável | Imagem lenta no dia do disparo é imagem que não aparece |

---

## A armadilha: nunca linkar para a branch

A URL óbvia aponta para a branch de trabalho:

```
.../zerohora-crm-ativacao/claude/zero-hora-neoprene-email-cegofj/imagens-design/...
```

**Essa URL morre quando o PR for mergeado e a branch apagada.** E aí não morre só no
futuro: morre em todo email já entregue, em toda caixa de entrada, de uma vez. Email não
tem como ser corrigido depois de enviado.

O mesmo vale, em menor grau, para `main`: basta alguém renomear uma pasta ou reorganizar
os arquivos meses depois para quebrar a peça inteira.

**A URL fixada em commit SHA é imutável.** O commit não muda de conteúdo, não é apagado
junto com a branch e não depende de ninguém manter a estrutura de pastas. É a única forma
de hospedar no GitHub sem deixar uma bomba-relógio no email.

---

## URLs de produção — commit `12e3a94`

| Arquivo | Peso | URL |
|---|---|---|
| `linha-hero-surfista-01.jpg` | 123 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/00-linha-neoprene/linha-hero-surfista-01.jpg |
| `linha-lifestyle-praia-01.jpg` | 194 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/00-linha-neoprene/linha-lifestyle-praia-01.jpg |
| `linha-lifestyle-surfista-02.jpg` | 233 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/00-linha-neoprene/linha-lifestyle-surfista-02.jpg |
| `camiseta-packshot-costas.jpg` | 128 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/01-camiseta-neoprene-cabo-frio/camiseta-packshot-costas.jpg |
| `camiseta-packshot-frente.jpg` | 137 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/01-camiseta-neoprene-cabo-frio/camiseta-packshot-frente.jpg |
| `bermuda-lifestyle-01.jpg` | 415 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/02-bermuda-neoprene-joaquina/bermuda-lifestyle-01.jpg |
| `bermuda-packshot-lateral.jpg` | 159 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/02-bermuda-neoprene-joaquina/bermuda-packshot-lateral.jpg |
| `sapatilha-packshot-lateral.jpg` | 69 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/03-sapatilha-esportiva-neoprene/sapatilha-packshot-lateral.jpg |
| `sapatilha-packshot-solado.jpg` | 105 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/03-sapatilha-esportiva-neoprene/sapatilha-packshot-solado.jpg |
| `logo-use-zero-hora-branco.png` | 29 KB | https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/12e3a949604025015185a31c1ddecbec0b6dc4a0/imagens-design/04-marca/logo-use-zero-hora-branco.png |
**Regra de uso:** copie a URL inteira, com o SHA. Nunca troque o SHA por um nome de
branch para "ficar mais limpo" — é exatamente aí que a peça quebra.

Se qualquer imagem for alterada ou adicionada depois deste commit, a lista precisa ser
regerada com o SHA novo, e o HTML atualizado antes do disparo.

---

## Verificação das 10 URLs — 10/08/2026

Todas testadas uma a uma. Nenhuma serve WebP, que é o formato que quebra no Outlook.

| Resultado | Arquivos |
|---|---|
| `200` + `image/jpeg` | as 9 fotografias |
| `200` + `image/png` | o logo |

---

## Ação obrigatória antes do merge: garantir que o SHA sobreviva

O commit `12e3a94` está hoje só na branch de trabalho. O que acontece com ele depende de
como o PR for mergeado:

- **Merge commit** — o commit entra na história da `main` e as URLs valem para sempre.
  **É a opção segura.**
- **Squash ou rebase** — o commit não entra na história da `main`. Ele costuma continuar
  resolvendo pelo ref que o GitHub mantém do PR, mas isso é comportamento de retenção não
  documentado, e não é coisa em que se aposte uma campanha inteira que já foi entregue.

Tentei criar e publicar um tag apontando para esse commit, que resolveria a questão de
forma definitiva. **O push de tag falha neste ambiente** — o proxy git só aceita a branch
designada.

Então escolha uma destas três, antes ou logo depois do merge:

1. **Mergear o PR com "Create a merge commit"**, não com squash. Resolve sozinho.
2. **Criar um tag pela interface do GitHub** apontando para `12e3a94`
   (Releases → Draft a new release → escolher o commit). Um tag mantém o commit
   alcançável para sempre, independente do que aconteça com a branch.
3. **Regerar esta lista com um SHA da `main` depois do merge** e atualizar o HTML antes
   do disparo. Só funciona se o email ainda não tiver sido enviado.

---

## Ressalvas honestas sobre esta escolha

**O `raw.githubusercontent.com` não é um CDN.** O GitHub não o oferece como serviço de
hospedagem para produção, e pode limitar tráfego pesado de hotlink. Para um disparo de
algumas centenas ou poucos milhares de aberturas, funciona. Para uma base grande, ou para
uma peça que vá ser reenviada, é frágil.

**Alternativa dentro do próprio GitHub:** publicar `imagens-design/` via GitHub Pages.
É o caminho que o GitHub de fato oferece para conteúdo estático, servido por CDN. Custa
uma configuração a mais e continua exigindo repositório público.

**A opção mais sólida continua sendo o CDN da própria loja.** Imagem servida do mesmo
domínio da marca não tem limite de hotlink, não depende de repositório público e é um
sinal marginalmente melhor para filtro de spam do que imagem vinda de um domínio de
hospedagem de código.

**Uma consequência que vale registrar:** hospedar aqui exige que este repositório
continue público. Ele não versiona PII — contato e export cru estão no `.gitignore` —
mas versiona a arquitetura de CRM da marca, os contratos de dados e a estratégia desta
campanha. É uma decisão de negócio, não técnica. Se preferir fechar o repositório, a
hospedagem precisa sair do GitHub antes.
