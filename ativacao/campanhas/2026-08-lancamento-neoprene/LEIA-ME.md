# Campanha — lançamento da linha neoprene (email marketing)

Peça: **um email HTML de lançamento** da linha de neoprene da Use Zero Hora, com três
produtos — camiseta Cabo Frio, bermuda Joaquina e sapatilha esportiva.

Objetivo: **conversão no site próprio**, não tráfego. As artes de origem ficam em
`imagens-design/`, organizadas por produto.

## Decisões fechadas

| Tema | Decisão |
|---|---|
| Audiência | Base masculina do site próprio. A lista já foi gerada pelo time. |
| Formato | Uma peça única de lançamento, com os três produtos, ancorada nas imagens principais e nos infográficos de features em destaque. |
| Ordem dos produtos | Definida por volume de busca (Etapa 2). Sem dado de busca, vale o que a arte já sustenta. |
| Features em destaque | Cruzamento entre dor de maior demanda nas buscas e o que a arte comprova. Feature sem lastro na arte não entra. |
| Oferta | Frete grátis **incondicional** — sem valor mínimo, região ou prazo. Claro e visível na peça, e não é o mote. Fora do assunto, do preheader e da primeira frase. Sem ressalva nem letra miúda: não há condição a escrever. |
| Fora da peça | **Sem preço e sem prazo de entrega.** Decisão editorial: o email vende pelo benefício de uso e pela tecnologia; o preço aparece na página do produto, depois do clique. |
| Uso das artes | Fotografia de produto e lifestyle são **assets** e entram no email. Infográficos são **referência de conteúdo** e não entram: deles sai a informação, e o tratamento visual das features é criado pelo Claude Design. |
| Data de disparo | **10/08/2026** |
| Ferramenta de disparo | **Mailmeteor**, sobre Gmail, com lista em Google Sheets |
| Handoff | Aqui sai documentação — fichas, arquitetura, copy, inventário de imagens e briefing. **O Claude Design faz layout, composição, posicionamento e o código.** |

## A restrição que domina a peça

O disparo por Mailmeteor sobre Gmail impõe o limite que mais restringe o layout: **o HTML
precisa ficar abaixo de 102 KB**. Acima disso o Gmail corta a peça no meio e esconde o
resto atrás de "ver mensagem inteira" — e o que fica escondido é o fim do email, onde
está o último call-to-action.

O alvo de trabalho é **80 KB**. A folga cobre o pixel de rastreio, o rodapé e a reescrita
de link que a ferramenta injeta no envio, depois de o arquivo já estar fechado.

A conta é de HTML e CSS inline; imagem hospedada por URL não entra nela. O que estoura o
limite é CSS repetido bloco a bloco — e a peça tem três blocos de produto de estrutura
parecida, que é o padrão que multiplica código. Isso está no briefing do Design como
restrição dominante, não como nota de rodapé.

Fontes: [limite de 102 KB do Gmail](https://www.emailonacid.com/blog/article/email-development/gmail-email-clipping/),
[alvo de 80 KB](https://tabular.email/blog/email-template-size-width-and-height),
[limites do Mailmeteor](https://mailmeteor.com/docs/help/troubleshooting/attachments-issues).

## Fonte de dados do produto

As **artes são a única fonte** de preço, medida, tecnologia, cor e tamanho. O site
`usezerohora.com.br` está bloqueado pelo proxy de egress deste ambiente, e o time
confirmou que todo o dado necessário está nas artes. O que não estiver na arte não entra
na peça — vira pendência registrada.

## Onde cada coisa mora

| Artefato | Caminho |
|---|---|
| Artes originais e assets | `imagens-design/<produto>/` |
| Prompt-mestre do projeto | `prompts/00-system-projeto.md` |
| Prompt de cada etapa | `prompts/etapa-N-*.md` |
| Fichas de produto extraídas das artes | `01-fichas-produto.md` |
| Demanda de busca e as duas decisões que ela sustenta | `02-demanda-keywords.md` |
| Arquitetura do email | `03-arquitetura-email.md` |
| Copy final por bloco | `04-copy.md` |
| Pacote de handoff para o Claude Design | `05-brief-design.md` |
| URLs de produção das imagens | `06-urls-imagens.md` |
| **Prompt pronto para colar no Claude Design** | `07-prompt-claude-design.md` |
| QA da peça entregue | `07-qa-disparo.md` |

## Etapas

| # | Etapa | Onde roda | Estado |
|---|---|---|---|
| 0 | Fundação — estrutura de pastas por produto | Claude Code | pronto |
| 1 | Extração das artes → ficha por produto | Claude Code | aguarda upload das artes |
| 2 | Demanda de busca → ordem dos produtos e das features | Claude Code + Semrush | **bloqueada: saldo Semrush zerado** |
| 3 | Arquitetura do email — blocos, função, hierarquia | Claude Code | depende de 1 e 2 |
| 4 | Copy — assunto, preheader, blocos, CTA | Claude Code | depende de 3 |
| 5 | Pacote de handoff — briefing, inventário de imagens, copy | Claude Code | depende de 4 |
| 6 | **Layout e código do email** | **Claude Design** | depende de 5 |
| 7 | QA — fidelidade de copy, limites, peça sem imagem, links | Claude Code | depende de 6 |

**A fronteira entre Claude Code e Claude Design está na Etapa 5/6.** Daqui sai o *quê* e
o *porquê* de cada bloco; do Claude Design vêm a solução visual e o HTML.

## Bloqueios abertos

1. **Artes não subidas.** Trava a Etapa 1, que trava todo o resto. É o caminho crítico.
2. **Semrush sem saldo** (`403 ERROR 132 :: API UNITS BALANCE IS ZERO`, 09/08/2026).
   Trava a Etapa 2. Alternativa sem custo: arquivar um export de volume de busca em
   `search-mkt/data/` — o prompt da Etapa 2 já lê dessa fonte. Sem nenhuma das duas, a
   ordem de produtos e features sai marcada como provisória, sustentada por julgamento
   declarado como tal.

## Prazo

Disparo em 10/08/2026, com as artes ainda não subidas em 09/08. As Etapas 1 e 3 a 5
rodam em sequência numa volta só assim que as imagens estiverem no repositório; a Etapa 2
sai como provisória, salvo crédito de Semrush ou export de volume até lá. O tempo de
layout e código do Claude Design entra depois disso, e é o que resta do prazo.

## Regras que a copy herda

Do playbook de CRM da marca (skill `zerohora-crm-copywriter`):

- Assunto até **50 caracteres**, sem emoji e sem "frete grátis" no gancho — os dois
  correlacionam negativo com conversão nos dados da marca.
- Primeira frase do corpo: **15 a 25 palavras** com dois benefícios funcionais mais um
  diferencial técnico concreto ("secagem em 20 minutos", não "qualidade superior").
- **Um único CTA** por mensagem, direto para `usezerohora.com.br`.
- Benefício funcional acima de apelo aspiracional.
- Duas variações A/B com abordagens realmente diferentes, não troca de palavra.

E do contrato de dados do repositório: **nenhuma PII versionada**, e todo número citado
(preço, medida, prazo) sai da arte, com data de coleta.
