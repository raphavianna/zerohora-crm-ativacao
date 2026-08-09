# Etapa 2 — Demanda de busca → ordem dos produtos e das features

**Entra:** `01-fichas-produto.md` + dados de volume de busca.
**Sai:** `02-demanda-keywords.md` + snapshot datado em `search-mkt/reports/`.

**Estado: bloqueada por saldo.** A conta Semrush retornou
`403 ERROR 132 :: API UNITS BALANCE IS ZERO` em 09/08/2026. O prompt está pronto para
disparar assim que houver crédito, ou assim que um export de volume for arquivado em
`search-mkt/data/`.

Esta etapa existe para responder duas perguntas, e só elas: **em que ordem os três
produtos aparecem no email**, e **quais features entram em destaque**. O volume de busca
é insumo dessas duas decisões, não regra sobre a copy.

---

## A) PROMPT

```
Levante a demanda de busca da linha de neoprene no Brasil e converta esse dado em duas
decisões de conteúdo do email. Esta é a Etapa 2: nenhuma copy é escrita aqui.

<fichas>
{{FICHAS_PRODUTO}}
</fichas>

<fonte_de_dados>
Fonte primária: Semrush, database "br", via o fluxo keyword_research →
get_report_schema → execute_report. Use phrase_these para volume, CPC e intenção em lote
(até 100 termos separados por ponto e vírgula), phrase_questions para as perguntas reais
do consumidor e phrase_related para expandir a cauda.

Fonte alternativa: qualquer export de volume arquivado em search-mkt/data/. Antes de usar
um export, perfile o arquivo — colunas, período, mercado, unidade — e registre a
proveniência.

Se nenhuma das duas estiver disponível, escreva "dado indisponível via Semrush" e produza
mesmo assim as duas decisões, marcadas como **provisórias**, sustentadas por julgamento
qualitativo declarado como tal. Uma decisão provisória e rotulada vale mais que uma
decisão adiada; uma decisão provisória e não rotulada é a única saída inaceitável.
</fonte_de_dados>

<o_que_levantar>
Três blocos de termos:

1. **Cabeça de produto** — os termos que nomeiam cada uma das três peças e suas
   variações naturais de nome. Serve para ordenar os produtos.
2. **Features e dores** — os termos que descrevem o problema que o neoprene resolve:
   água fria, proteção solar, aderência em pedra, secagem, espessura, caimento. Serve
   para ordenar as features.
3. **Perguntas reais** — o que o consumidor de fato digita em forma de pergunta sobre
   neoprene. É aqui que a dor aparece com as palavras do cliente, e é o bloco de maior
   valor para a copy.

Para cada termo registre volume, CPC, densidade competitiva e intenção. Registre também
a data de coleta e a base.
</o_que_levantar>

<as_duas_decisoes>
**Decisão 1 — ordem dos produtos no email.** Some o volume dos termos de cabeça de cada
peça e ordene. Mostre a conta. O produto de maior demanda ocupa o primeiro bloco depois
do hero.

Antes de fechar, confronte o número com uma checagem de sentido: o produto de maior
volume de busca é o de maior demanda *desta base*? Volume de busca mede o mercado
brasileiro inteiro, não a base masculina do site próprio da marca. Quando houver
divergência plausível entre os dois, registre-a e recomende explicitamente qual sinal
seguir.

**Decisão 2 — features em destaque.** Cruze as features que as fichas da Etapa 1
sustentam com os termos de dor de maior volume. Uma feature entra em destaque quando ela
tem demanda de busca **e** existe na arte. Feature com demanda e sem lastro na arte vira
pedido ao time, não texto. Feature sem demanda mas presente na arte entra em segundo
plano, e é o que preenche quando não houver dado de busca para o produto.
</as_duas_decisoes>

Antes de decidir, raciocine em <thinking>: agrupe os termos por peça, aponte os
canibalizados entre dois produtos (um termo genérico de neoprene não pertence a nenhuma
peça isolada) e resolva a atribuição.

Produza 02-demanda-keywords.md com:
1. Tabela de termos: termo, volume, CPC, intenção, produto a que se liga, fonte, data
2. As perguntas reais, agrupadas por dor
3. Decisão 1 com a conta à vista e o confronto com a base
4. Decisão 2 com a tabela de cruzamento feature × demanda × lastro na arte
5. Features com demanda e sem lastro — a lista de pedidos ao time
6. Vocabulário para a copy: as palavras que o consumidor usa, para a Etapa 4 preferi-las
   às palavras internas da marca

E salve o retorno bruto das chamadas como snapshot datado em search-mkt/reports/, para
que nenhuma sessão futura pague de novo pelo mesmo dado.
```

---

## B) RACIONAL TÉCNICO

- **Escopo fechado logo na primeira linha** ("duas decisões, e só elas"). Pesquisa de
  keyword sem pergunta definida vira relatório de 200 termos que ninguém usa.
- **Fonte primária, alternativa e saída declarada** nessa ordem: é o protocolo do
  `CLAUDE.md` do `search-mkt` transposto para o prompt, com a saída — "dado indisponível
  via Semrush" — presente por escrito, porque hoje ela é o caminho provável.
- **A instrução "provisória e rotulada vale mais que adiada"** existe para impedir a
  falha mais cara aqui: o modelo travar a campanha inteira esperando um crédito.
- **Confronto volume de mercado × demanda da base**: o dado da Semrush é do Brasil
  inteiro; a lista é da base masculina do site. Sem esse confronto explícito, a ordem dos
  produtos é decidida por um número que não descreve o público que vai receber o email.
- **Regra de lastro** (feature só entra em destaque se tem demanda **e** existe na arte)
  liga esta etapa à `<regra_de_evidencia>` do prompt-mestre. É o que impede que o volume
  de busca puxe para a peça um benefício que o produto não tem.
- **Snapshot obrigatório**: crédito de ferramenta é recurso finito, e hoje está em zero.

## C) VARIÁVEIS

| Variável | O que recebe |
|---|---|
| `{{FICHAS_PRODUTO}}` | Conteúdo de `01-fichas-produto.md` |

## E) COMO TESTAR

Sucesso: a Decisão 1 mostra a soma de volume por peça, e não só o resultado. Se a saída
disser "a bermuda vem primeiro porque tem mais busca" sem os números, o critério não é
auditável e a decisão não vale.

Caso de teste: rode com a Semrush sem saldo. A saída correta traz as duas decisões
marcadas como provisórias com o julgamento declarado — não uma recusa, e não um número
inventado.
