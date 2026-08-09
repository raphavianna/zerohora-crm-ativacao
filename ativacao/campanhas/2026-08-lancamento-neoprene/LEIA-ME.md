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
| Oferta | Frete grátis: claro e visível na peça, e não é o mote. Fora do assunto, do preheader e da primeira frase. |
| Handoff | Aqui sai documentação — fichas, arquitetura, copy, inventário de imagens e briefing. **O Claude Design faz layout, composição, posicionamento e o código.** |

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

1. **Artes não subidas.** Trava a Etapa 1, que trava todo o resto.
2. **Semrush sem saldo** (`403 ERROR 132 :: API UNITS BALANCE IS ZERO`, 09/08/2026).
   Trava a Etapa 2. Alternativa sem custo: arquivar um export de volume de busca em
   `search-mkt/data/` — o prompt da Etapa 2 já lê dessa fonte. Sem nenhuma das duas, a
   ordem de produtos e features sai marcada como provisória.
3. **Condições do frete grátis** não definidas: valor mínimo, região e validade.
4. **Ferramenta de disparo** não confirmada (o playbook cita Brevo na fase 1). Define as
   tags de personalização e o link de descadastro que o Design precisa embutir no HTML.

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
