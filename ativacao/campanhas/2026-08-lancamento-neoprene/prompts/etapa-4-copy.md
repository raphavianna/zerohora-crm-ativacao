# Etapa 4 — Copy

**Entra:** `01-fichas-produto.md` + `02-demanda-keywords.md` + `03-arquitetura-email.md`.
**Sai:** `04-copy.md`.

Escreve o texto final de cada bloco definido na Etapa 3. É a etapa que a skill
`zerohora-crm-copywriter` governa — as regras de caractere e de estrutura vêm dela.

---

## A) PROMPT

```
Escreva a copy final do email de lançamento da linha de neoprene, bloco a bloco, seguindo
a arquitetura já aprovada.

<arquitetura>
{{ARQUITETURA}}
</arquitetura>

<fichas>
{{FICHAS_PRODUTO}}
</fichas>

<vocabulario_do_consumidor>
{{VOCABULARIO}}
</vocabulario_do_consumidor>

<regras>
Valem para todos os blocos da peça, não só para o primeiro:

- Assunto: até 50 caracteres, sem emoji, sem "frete grátis". É só o gancho que ganha a
  abertura.
- Preheader: até 90 caracteres, complementa o assunto em vez de repeti-lo, sem "frete
  grátis".
- Primeira frase do corpo: de 15 a 25 palavras, com dois benefícios funcionais mais um
  diferencial técnico concreto.
- Diferencial técnico é número ou mecanismo que veio da ficha. Adjetivo vago não conta.
- Um único call-to-action, para usezerohora.com.br, repetível fisicamente mas sempre a
  mesma ação.
- O bloco de frete grátis é claro e direto, e não abre a peça.
- Prefira a palavra que o consumidor digita à palavra interna da marca, quando as duas
  descreverem a mesma coisa e a do consumidor estiver no vocabulário acima.
- Declare a contagem de caracteres ao lado do assunto e do preheader.
</regras>

<exemplos>
Os exemplos abaixo usam a categoria Poncho, de propósito: eles ensinam a **forma**, e
seus números não pertencem à linha de neoprene. Nunca transporte um número daqui para a
peça — todo número da peça sai das fichas.

<exemplo>
Contexto: assunto de email de lançamento.
Ruim: "🌊 Chegou o poncho novo com frete grátis!"
Por quê: emoji, e "frete grátis" em posição de gancho.
Bom: "Poncho novo: troca de roupa em pé na areia" (41 caracteres)
Por quê: gancho concreto, no benefício de uso, dentro do limite.
</exemplo>

<exemplo>
Contexto: primeira frase do corpo.
Ruim: "Sinta-se livre e radiante com a qualidade superior do nosso novo poncho."
Por quê: apelo aspiracional e adjetivo vago; nenhum benefício funcional, nenhum número.
Bom: "Felpa dupla que puxa a água do corpo em segundos e capuz fundo que segura o vento,
em algodão de 380 g/m² que seca pendurado." (22 palavras)
Por quê: dois benefícios funcionais mais um diferencial técnico com número.
</exemplo>

<exemplo>
Contexto: bloco de produto com dado faltando na ficha.
Situação: a ficha registra "espessura: não consta na arte".
Ruim: "Neoprene de 2 mm, a espessura ideal para a água brasileira."
Por quê: o número foi inventado para preencher a lacuna.
Bom: escrever o bloco com os atributos que a ficha sustenta e listar a espessura como
pendência de arte no fim do documento.
</exemplo>

<exemplo>
Contexto: as duas variações A/B do assunto.
Ruim: "Poncho novo chegou" e "O poncho novo chegou"
Por quê: as duas testam a mesma coisa; a diferença é uma palavra.
Bom: "Poncho novo: troca de roupa em pé na areia" contra "Últimas 40 unidades do poncho
novo"
Por quê: uma testa benefício de uso, a outra testa escassez. O resultado ensina algo.
</exemplo>
</exemplos>

<lacunas>
Quando a arquitetura pedir um bloco que as fichas não sustentam, escreva o bloco com o
que existe e registre a pendência. Não invente número, material, prazo nem prova para
fechar a frase. Bloco incompleto e sinalizado é corrigível; bloco completo e inventado
chega no cliente.
</lacunas>

Antes de escrever, raciocine em <thinking>: identifique, para cada produto, qual dor do
vocabulário do consumidor aquele produto resolve melhor, e verifique se a ficha sustenta
essa promessa. Copy que promete o que a ficha não sustenta é reescrita, não ajustada.

Produza 04-copy.md com:
1. Assunto — duas variações A/B com abordagens diferentes entre si, com contagem de
   caracteres
2. Preheader — duas variações, com contagem
3. Copy de cada bloco, na ordem da arquitetura, identificado pelo nome do bloco
4. Texto alternativo de cada imagem, descrevendo a informação e não a aparência
5. Texto do call-to-action
6. Versão em texto puro da peça, para o fallback
7. Pendências: o que ficou sem lastro na ficha
```

---

## B) RACIONAL TÉCNICO

- **Few-shot com quatro exemplos diversos** (Cap. 7) — a alavanca isolada mais efetiva
  aqui. Cada um cobre um modo de falha diferente: gancho, primeira frase, lacuna de dado
  e A/B falso. Cada exemplo traz o par ruim/bom **com o motivo**, porque o motivo é o que
  transfere para o caso que o exemplo não cobre.
- **Exemplos deliberadamente em Poncho**, com aviso explícito. Exemplo em neoprene com
  número plausível é um vetor de contaminação: o modelo copia "2 mm" para a peça real. A
  troca de categoria torna a contaminação impossível de passar despercebida.
- **O terceiro exemplo ensina o comportamento na lacuna**, que é onde a alucinação
  aparece em copy de produto — a frase pede um número, e o modelo fornece um.
- **O quarto exemplo ataca o A/B decorativo**, o vício mais comum de teste em CRM: duas
  variações que trocam uma palavra não produzem aprendizado nenhum.
- **Contagem de caractere declarada ao lado**: o limite é a parte da entrega que quebra
  em silêncio, e assunto cortado na caixa de entrada é defeito, não detalhe.
- **Versão em texto puro** entra como item de entrega, não como sobra.

## C) VARIÁVEIS

| Variável | O que recebe |
|---|---|
| `{{ARQUITETURA}}` | Conteúdo de `03-arquitetura-email.md` |
| `{{FICHAS_PRODUTO}}` | Conteúdo de `01-fichas-produto.md` |
| `{{VOCABULARIO}}` | Seção de vocabulário do consumidor de `02-demanda-keywords.md` |

## E) COMO TESTAR

Sucesso, em três checagens binárias: nenhum assunto passa de 50 caracteres; a primeira
frase do corpo tem entre 15 e 25 palavras contadas na mão; e cada número da peça é
rastreável a uma linha da ficha.

Caso de teste: apague um dado da ficha de um produto — a espessura, por exemplo — e rode
de novo. A copy correta reescreve o bloco sem o número e registra a pendência. Se ela
devolver um número, o `<lacunas>` não pegou e a peça não pode ir para o Design.
