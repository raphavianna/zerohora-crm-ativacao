# Etapa 1 — Extração das artes → ficha por produto

**Entra:** as imagens de `imagens-design/`.
**Sai:** `01-fichas-produto.md`.
**Depende de:** as artes estarem subidas. Nada mais.

As artes são a **única fonte** de preço, medida, tecnologia, cor e tamanho nesta campanha
(a página do produto está inacessível a partir deste ambiente). O que não estiver na arte
não existe na peça.

---

## A) PROMPT

```
Leia as artes da linha de neoprene e transforme cada uma em ficha de produto estruturada.
Esta é a Etapa 1: nenhuma copy de email é escrita aqui.

<artes>
{{ARTES}}
</artes>

<produtos>
1. Camiseta de neoprene Cabo Frio — imagens-design/01-camiseta-neoprene-cabo-frio/
2. Bermuda de neoprene Joaquina — imagens-design/02-bermuda-neoprene-joaquina/
3. Sapatilha esportiva de neoprene — imagens-design/03-sapatilha-esportiva-neoprene/
Artes da linha inteira (tecnologia, medidas, hero) — imagens-design/00-linha-neoprene/
</produtos>

<o_que_extrair>
Para cada produto, percorra todas as artes dele antes de escrever qualquer campo:

- Nome exato como aparece na arte
- Preço, à vista e parcelado, exatamente como escrito
- Material e composição
- Espessura do neoprene
- Tecnologias nomeadas na arte (costura, forro, tratamento, proteção UV)
- Tamanhos ou numeração disponíveis
- Cores disponíveis
- Claims funcionais: cada frase de benefício que a arte afirma, transcrita literalmente
- Números: qualquer medida, percentual, prazo ou temperatura que a arte exiba
- Frete e prazo de envio, se a arte mencionar
- Provas: avaliação, selo, garantia, depoimento

Depois, para a linha como um todo, extraia o que as artes de 00-linha-neoprene afirmam
sobre a tecnologia do neoprene e sobre a tabela de medidas.
</o_que_extrair>

<infograficos>
Separe, entre tudo que você leu, o que deve **sobreviver como imagem** no email e o que
deve **virar texto**.

Sobrevive como imagem quando a informação é comparativa, dimensional ou espacial — uma
tabela de medidas, um corte que mostra as camadas do neoprene, um mapa de costura, uma
grade de numeração. Traduzir isso para frase destrói a informação.

Vira texto quando é uma afirmação única que cabe em uma linha — "secagem rápida",
"proteção UV50". Manter isso como imagem esconde a mensagem de quem lê com imagem
bloqueada, que é a maioria em primeira abertura.

Para cada infográfico que sobrevive, registre o caminho exato do arquivo e escreva o
texto alternativo que descreve a informação que ele carrega, não a aparência dele.
</infograficos>

<lacunas>
Quando um campo não aparecer em nenhuma arte do produto, escreva exatamente "não consta
na arte". Não infira a partir do nome do produto, do que é usual em neoprene, do que os
outros dois produtos têm, nem do que faria sentido comercialmente. A lacuna registrada é
um resultado útil: ela vira pedido de arte nova ou de dado ao time.
</lacunas>

Antes de escrever a ficha, raciocine em <thinking>: liste as artes que você leu por
produto, aponte onde duas artes se contradizem (preço diferente, medida diferente) e
decida qual prevalece, declarando o motivo. Divergência não resolvida vira linha na
seção de lacunas, não escolha silenciosa.

Depois produza o arquivo 01-fichas-produto.md com esta estrutura, uma seção por produto e
uma seção final da linha:

## <nome do produto>
**Artes lidas:** <caminhos>
**Preço:** <valor> _(coletado da arte em {{DATA}})_
**Material e espessura:** ...
**Tecnologias:** ...
**Tamanhos / numeração:** ...
**Cores:** ...
**Claims transcritos da arte:**
- "<frase literal>" — <arquivo>
**Números disponíveis:** ...
**Provas:** ...
**Infográficos que sobrevivem como imagem:**
| Arquivo | Informação que carrega | Texto alternativo |
**Lacunas:** ...

## Linha neoprene — comum aos três
...

## Lacunas que bloqueiam a copy
Lista única, priorizada, do que falta e de qual arte resolveria.
```

---

## B) RACIONAL TÉCNICO

- **Dados no topo, tarefa no fim** (Cap. 8): as artes abrem o prompt porque são a entrada
  volumosa; a instrução de formato fecha.
- **Precognition** (Cap. 6) com um trabalho específico: resolver contradição entre artes.
  Sem isso, o modelo pega o primeiro preço que vê e segue.
- **"Não consta na arte" como saída legítima** (Cap. 8) repetido aqui, com a lista de
  inferências proibidas nomeada uma a uma. A regra genérica não segura o caso em que os
  outros dois produtos têm o dado — é a lacuna mais fácil de preencher por engano.
- **Critério de decisão explícito para infográfico** (comparativo/dimensional/espacial
  fica imagem; afirmação única vira texto), com o motivo declarado. Critério com motivo
  transfere; regra sem motivo vira sorteio no caso limítrofe.
- **Texto alternativo pela informação, não pela aparência**: em email, imagem bloqueada é
  o estado default da primeira abertura, e o alt é a mensagem, não uma legenda.

## C) VARIÁVEIS

| Variável | O que recebe |
|---|---|
| `{{ARTES}}` | As imagens de `imagens-design/`, anexadas ou referenciadas por caminho |
| `{{DATA}}` | Data da leitura, para carimbar preço e oferta (mudam) |

## E) COMO TESTAR

Sucesso: a ficha traz **caminho de arquivo em cada claim** e a seção de lacunas não está
vazia. Ficha sem lacuna nenhuma, em três produtos, é sinal de preenchimento por inferência
— vale reler.

Caso de teste: se a arte da sapatilha não mostrar espessura do neoprene, o campo precisa
sair como "não consta na arte", **mesmo que** a camiseta e a bermuda mostrem a delas.
