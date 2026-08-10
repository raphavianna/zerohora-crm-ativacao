# Etapa 3 — Arquitetura do email

Define quais blocos existem, em que ordem e por quê. Nenhuma decisão visual aqui.

---

## Estratégia da peça: a linha primeiro, depois as peças

Três produtos competem por atenção com os outros dois. Duas saídas eram possíveis:
abrir pelo produto-âncora e usar os outros dois como complemento, ou vender a linha e
depois abrir as peças.

**Escolha: linha primeiro.** O que sustenta:

1. O **neoprene de 1,5 mm** é o único atributo que os três produtos comprovam. É o que
   transforma três lançamentos soltos em um lançamento de linha, e um argumento único
   sustenta a dobra melhor que três argumentos disputando espaço.
2. A única arte que mostra os três produtos juntos — `linha-lifestyle-praia-01.jpg`,
   surfista de costas com camiseta, bermuda e sapatilhas — existe e é boa. Abrir pelo
   produto-âncora desperdiçaria o melhor asset do acervo.
3. O CTA é único e leva à coleção, não a um produto. Uma peça que abre por um produto e
   entrega o clique numa coleção cria uma quebra de expectativa no meio do caminho.

**Custo assumido:** a peça vende três produtos com menos profundidade em cada um do que
se fosse um email por produto. É a troca correta num lançamento de linha, e o follow-up
por produto resolve a profundidade depois, para quem clicar.

---

## Os três leitores

| Leitor | O que ele precisa absorver | Onde a arquitetura entrega |
|---|---|---|
| Lê só assunto e preheader | Que a Use Zero Hora lançou uma linha de neoprene de 1,5 mm, com três peças | Blocos 1 e 2 |
| Abre, olha e rola até o meio | Hero da linha, o argumento do 1,5 mm, o frete grátis e a primeira peça | Blocos 3 a 7 |
| Lê tudo | As três peças com suas features, e o fechamento da linha | Blocos 3 a 11 |

O corte do leitor do meio caiu depois do bloco da camiseta de propósito: ele sai sabendo
o que é a linha, que o frete é grátis e como é a peça mais universal dela.

---

## Blocos

| # | Bloco | Função | Conteúdo | Imagens | Peso | Sem imagem |
|---|---|---|---|---|---|---|
| 1 | Assunto | Ganhar a abertura | Gancho curto, sem preço e sem frete grátis | — | dominante | íntegro |
| 2 | Preheader | Complementar o assunto | Nomeia as três peças ou o contexto de uso | — | apoio | íntegro |
| 3 | Topo | Identificar o remetente | Logo Use Zero Hora | logo (pendente) | secundário | precisa do nome em texto |
| 4 | Hero da linha | Comunicar lançamento de linha de neoprene | Headline do lançamento sobre a foto dos três produtos em uso | `00-linha-neoprene/linha-lifestyle-praia-01.jpg` | **dominante** | a headline em texto carrega o bloco sozinha |
| 5 | Argumento da linha | Dar a razão de compra em uma frase | A frase de abertura com o 1,5 mm, o conforto térmico e a liberdade de movimento | — | **dominante** | íntegro, é texto |
| 6 | CTA | Levar ao site | Botão único para a coleção | — | dominante | íntegro se for texto com link, não imagem |
| 7 | Frete grátis | Remover atrito antes das peças | Frete grátis para todo o Brasil, sem valor mínimo | — | apoio | íntegro |
| 8 | Camiseta Cabo Frio | Vender a peça mais universal | Nome, três features, foto | `camiseta-packshot-frente.jpg` | apoio | o texto das features carrega |
| 9 | Bermuda Joaquina | Vender o par natural da camiseta | Nome, três features, foto | `bermuda-lifestyle-01.jpg` | apoio | idem |
| 10 | Sapatilha esportiva | Vender por descoberta | Nome, três features, foto do solado | `sapatilha-packshot-solado.jpg` | apoio | idem |
| 11 | Fechamento da linha | Reamarrar as três peças | Retoma o 1,5 mm como assinatura da linha | `camiseta-packshot-costas.jpg` ou `bermuda-packshot-lateral.jpg`, a critério do Design | apoio | íntegro |
| 12 | CTA final | Levar ao site | Mesmo botão, mesmo destino do bloco 6 | — | dominante | íntegro se for texto com link |
| 13 | Rodapé | Cumprir a obrigação legal e fechar | Marca, contato, descadastro | — | secundário | íntegro |

**Assets não usados na arquitetura:** `camiseta-packshot-costas.jpg`,
`bermuda-packshot-lateral.jpg` e `sapatilha-packshot-lateral.jpg` ficam disponíveis para
o Design usar no bloco 11 ou onde a composição pedir. Não sobra imagem inutilizada por
descuido: sobra por folga deliberada.

---

## Wireframe verbal

A peça abre com o logo da marca. Logo abaixo, ocupando a dobra inteira, a foto de um
surfista de costas na beira do mar, de camiseta preta de manga longa, bermuda e
sapatilhas, com a prancha debaixo do braço — e sobre ela a headline que anuncia a linha
de neoprene. Em seguida, uma frase única explica o que a linha faz: neoprene de 1,5 mm
nas três peças, que segura o calor do corpo contra o vento e a água fria e acompanha o
movimento. Vem o botão que leva à coleção.

Abaixo do botão, uma faixa curta informa que o frete é grátis para todo o Brasil, sem
valor mínimo. Ela é visível, mas não é o argumento da peça — está ali para tirar um
atrito de decisão, depois de a razão de compra já ter sido dada.

Então as três peças aparecem em sequência, cada uma com o nome, a foto e três coisas que
ela resolve. Primeiro a camiseta Cabo Frio, com o neoprene do corpo, a proteção solar das
mangas e o punho que impede a manga de subir. Depois a bermuda Joaquina, com a barra que
absorve menos água e seca mais rápido, o cordão que fica escondido no cós e a costura que
não atrita. Por último a sapatilha, mostrada pelo solado, com a aderência, os três
tecidos e o isolamento térmico.

A peça fecha reamarrando as três no mesmo ponto — 1,5 mm de neoprene — e repete o botão,
que leva ao mesmo lugar do primeiro. No rodapé, a marca e o link de descadastro.

---

## Tensões registradas

**Um único CTA contra três produtos.** A regra da marca é um CTA por mensagem, para o
site. Isso significa que os blocos de produto **não** ganham link próprio: os três levam
à mesma coleção. Para um lançamento de linha isso é coerente, e é o que está desenhado.
Mas é a primeira hipótese que vale testar no próximo disparo — link por produto costuma
converter melhor quando a pessoa já sabe qual peça quer, e aqui não dá para saber sem
medir.

**O frete grátis depois do argumento, não antes.** Posição definida pelos dados da marca,
não por gosto. Fica visível e sozinho num bloco, o que resolve o pedido de "claro e
visível" sem colocá-lo na posição que correlaciona negativo com conversão.

---

## O que ficou de fora

- **Bloco de tabela de medidas.** Não existe arte, e o dado não foi fornecido. É a maior
  objeção não respondida da peça: roupa de água colada ao corpo sem informação de tamanho.
- **Bloco de prova social.** Nenhuma avaliação, selo ou depoimento em nenhuma arte.
- **Preço e prazo de entrega.** Fora por decisão editorial, não por falta de dado.
- **Bloco institucional sobre a marca.** Não tem função numa peça de lançamento com CTA
  único; ocuparia espaço competindo com os produtos.
