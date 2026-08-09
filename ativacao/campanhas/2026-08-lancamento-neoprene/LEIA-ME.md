# Campanha — lançamento da linha neoprene (email marketing)

Peça: **um email HTML de lançamento** da linha de neoprene da Use Zero Hora, com três
produtos — camiseta Cabo Frio, bermuda Joaquina e sapatilha esportiva.

Objetivo: **conversão no site próprio**, não tráfego. As artes de origem ficam em
`imagens-design/`, organizadas por produto.

## Onde cada coisa mora

| Artefato | Caminho |
|---|---|
| Artes originais e assets | `imagens-design/<produto>/` |
| Fichas de produto extraídas das artes | `01-fichas-produto.md` |
| Insight de demanda (keywords) | `02-demanda-keywords.md` (snapshot bruto em `search-mkt/reports/`) |
| Arquitetura do email (blocos, hierarquia, wireframe) | `03-arquitetura-email.md` |
| Copy final por bloco | `04-copy.md` |
| Briefing de layout para o Claude Design | `05-brief-design.md` |
| Email HTML pronto para disparo | `06-email.html` |
| QA e checklist de envio | `07-qa-disparo.md` |
| Prompts de cada etapa | `prompts/` |

## Etapas

Cada etapa tem um prompt próprio em `prompts/`. Uma etapa por vez; o resultado é
apresentado e aprovado antes de a seguinte começar.

| # | Etapa | Onde roda | Entrega |
|---|---|---|---|
| 0 | Fundação — estrutura de pastas por produto | este repo | `imagens-design/` (pronto) |
| 1 | Extração das artes — ler cada peça, tirar claim, medida, tecnologia, cor, preço; marcar quais infográficos sobrevivem como imagem | Claude Code | `01-fichas-produto.md` |
| 2 | Insight de demanda — termos de maior volume no BR para o vocabulário da copy | Claude Code + Semrush, via `search-mkt` | `02-demanda-keywords.md` |
| 3 | Arquitetura do email — audiência, hierarquia de blocos, wireframe em texto | Claude Code | `03-arquitetura-email.md` |
| 4 | Copy — assunto, preheader, headline, bloco por produto, CTA | Claude Code + skill `zerohora-crm-copywriter` | `04-copy.md` |
| 5 | **Briefing de layout** — spec visual completa, sem escrever HTML | Claude Code | `05-brief-design.md` |
| 6 | **Layout** — direção visual, grid, tokens, tratamento dos infográficos | **Claude Design** | mock/spec visual aprovado |
| 7 | Build HTML — tabelas, CSS inline, 600 px, dark mode, alt text | Claude Code | `06-email.html` |
| 8 | QA e disparo — render, peso, links com UTM, fallback em texto | Claude Code | `07-qa-disparo.md` |

**A fronteira entre Claude Code e Claude Design é a Etapa 5/6.** Daqui sai a
especificação (o *quê* e o *porquê* de cada bloco); do Claude Design vem a direção
visual (o *como parece*). A Etapa 7 só começa com o layout aprovado — o HTML é a
tradução do layout, nunca a invenção dele.

## Regras que a copy herda

Do playbook de CRM da marca (skill `zerohora-crm-copywriter`):

- Assunto até **50 caracteres**, sem emoji e sem "Frete Grátis" no gancho — os dois
  correlacionam negativo com conversão nos dados da marca.
- Primeira frase do corpo: **15 a 25 palavras** com dois benefícios funcionais mais um
  diferencial técnico concreto ("secagem em 20 minutos", não "qualidade superior").
- **Um único CTA** por mensagem, direto para `usezerohora.com.br`.
- Benefício funcional acima de apelo aspiracional.
- Duas variações A/B com abordagens realmente diferentes, não troca de palavra.

E do contrato de dados do repositório: **nenhuma PII versionada**, e todo número citado
(preço, medida, prazo) sai da arte ou da página do produto, com data de coleta.
