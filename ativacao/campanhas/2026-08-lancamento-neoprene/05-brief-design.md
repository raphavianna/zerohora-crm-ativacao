# Briefing de layout — email de lançamento da linha neoprene

**Para: Claude Design.** Documento autossuficiente: tudo que é preciso para desenhar e
codificar a peça está aqui. Data: 09/08/2026. Disparo previsto: 10/08/2026.

---

## 1. O trabalho

Um email HTML de lançamento da linha de neoprene da Use Zero Hora — marca D2C brasileira
de surf e beachwear —, com três produtos: camiseta Cabo Frio, bermuda Joaquina e
sapatilha esportiva.

Vai para a base masculina do site próprio, por Mailmeteor sobre Gmail. O objetivo é venda
no site: o sucesso da peça é clique na coleção de neoprene, não abertura.

**O que faria a peça falhar:** ser cortada pelo Gmail antes do fim (limite de 102 KB);
chegar vazia para quem lê com imagem bloqueada; ou perder o argumento único da linha — o
neoprene de 1,5 mm — em meio a três produtos disputando atenção.

---

## 2. Inventário de imagens

### 2.1 Assets do email — nove fotografias e três variações de logo

| Arquivo | Bloco | Função | Texto alternativo |
|---|---|---|---|
| `imagens-design/04-marca/logo-use-zero-hora-branco.png` | 3 — Topo | **Recomendado.** Logo com lettering, branco — exige header escuro | Use Zero Hora |
| `imagens-design/04-marca/logo-use-zero-hora-redondo.png` | 3 — Topo | Alternativa: símbolo dentro de disco branco próprio, legível sobre qualquer fundo, sem lettering | Use Zero Hora |
| `imagens-design/04-marca/logo-use-zero-hora-preto.png` | 3 — Topo | Alternativa: logo com lettering, preto — exige header claro | Use Zero Hora |
| `imagens-design/00-linha-neoprene/linha-hero-surfista-01.jpg` | 4 — Hero | Abrir a peça; formato horizontal com espuma à esquerda como área livre para a headline | Surfista saindo do mar de camiseta de neoprene de manga longa e bermuda de neoprene, com a prancha debaixo do braço |
| `imagens-design/00-linha-neoprene/linha-lifestyle-praia-01.jpg` | 11 — Fechamento | Provar que a linha tem três peças, sapatilhas incluídas | Surfista de costas na beira do mar usando a linha completa: camiseta de neoprene de manga longa, bermuda e sapatilhas nos pés |
| `imagens-design/00-linha-neoprene/linha-lifestyle-surfista-02.jpg` | livre | Vertical de corpo inteiro da mesma sessão do hero | Surfista de corpo inteiro na beira do mar, de camiseta de neoprene de manga longa e bermuda de neoprene |
| `imagens-design/01-camiseta-neoprene-cabo-frio/camiseta-packshot-frente.jpg` | 8 — Camiseta | Mostrar a peça | Camiseta de neoprene Cabo Frio de frente, manga longa e gola alta, na cor preta |
| `imagens-design/01-camiseta-neoprene-cabo-frio/camiseta-packshot-costas.jpg` | 11 ou livre | Segundo ângulo da camiseta | Camiseta de neoprene Cabo Frio de costas, com recorte raglã e costura central |
| `imagens-design/02-bermuda-neoprene-joaquina/bermuda-lifestyle-01.jpg` | 9 — Bermuda | Mostrar o caimento vestido | Bermuda de neoprene Joaquina vestida, comprimento acima do joelho, na cor preta |
| `imagens-design/02-bermuda-neoprene-joaquina/bermuda-packshot-lateral.jpg` | 11 ou livre | Detalhe da bermuda | Detalhe lateral da bermuda de neoprene Joaquina, com a etiqueta emborrachada junto à barra |
| `imagens-design/03-sapatilha-esportiva-neoprene/sapatilha-packshot-solado.jpg` | 10 — Sapatilha | Provar o solado antiderrapante, que é o argumento da peça | Solado da sapatilha de neoprene visto de baixo, com a textura antiderrapante cobrindo toda a base |
| `imagens-design/03-sapatilha-esportiva-neoprene/sapatilha-packshot-lateral.jpg` | 11 ou livre | Mostrar a forma da sapatilha | Sapatilha de neoprene de perfil, com cano na altura do tornozelo |

Fotos em JPG. As três da linha têm 1200 px de largura; os packshots de produto, 1024 px.
Os três produtos são pretos.

**Sobre o logo — três opções, a escolha é sua.** Todas em PNG com alfa real.

- **Branco (recomendado).** Traz o nome da marca por extenso e exige header escuro. O
  dark mode do Gmail costuma escurecer fundo claro e deixar fundo já escuro em paz, então
  header escuro com logo branco é o arranjo que menos depende de como o cliente trata cor.
- **Redondo.** Só o símbolo, dentro de um disco branco próprio, o que o torna legível
  sobre qualquer fundo, claro ou escuro. Perde o lettering. É a escolha se você quiser
  header claro sem se preocupar com dark mode.
- **Preto.** Lettering completo para header claro, com a ressalva de que o dark mode pode
  escurecer o fundo do bloco e sumir com ele.

O texto alternativo é `Use Zero Hora` nos três, então a marca chega mesmo com imagem
bloqueada.

**Sobre as duas fotos de 10/08** (`linha-hero-surfista-01`, `linha-lifestyle-surfista-02`):
chegaram com marca d'água de IA, já removida por corte, e as versões arquivadas estão
limpas. Fica uma restrição: nelas, o texto de marca aplicado nas peças está embaralhado —
o selo circular no peito tem letras ilegíveis e a etiqueta na coxa é um borrão. Na largura
do email o selo fica com cerca de 30 px e lê como selo. **Não ampliar nem recortar o peito
ou a etiqueta da coxa.**

### 2.2 Referências de conteúdo — NÃO entram no email

Os nove infográficos em `imagens-design/<produto>/referencia/`. São peças com título,
ícones e texto aplicado, feitas para a página de produto. Existem aqui para você ver
**como a marca já comunicou cada feature** — linguagem, nível de detalhe, o que ela
escolhe destacar. Não são asset: o tratamento visual das features nesta peça é criação
sua, a partir da copy da seção 3.

Duas delas têm erro (um typo, uma grafia divergente de nome), o que é mais uma razão para
não recortá-las.

---

## 3. Copy por bloco, pronta para colar

**Assunto** — duas variações para teste A/B:
- A: `O frio da água não encurta mais a sessão` (40 caracteres)
- B: `Chegou a linha de neoprene 1,5 mm` (33 caracteres)

**Preheader** — duas variações:
- A: `Camiseta, bermuda e sapatilha em 1,5 mm. Feitas para água fria, vento e sol forte.` (82)
- B: `Camiseta Cabo Frio, bermuda Joaquina e sapatilha esportiva. As três em neoprene.` (80)

**Bloco 4 — Hero**
- Headline: `A linha de neoprene chegou`
- Apoio: `Camiseta, bermuda e sapatilha. As três em 1,5 mm.`

**Bloco 5 — Argumento da linha**
> Neoprene de 1,5 mm nas três peças: segura o calor do corpo contra o vento e a água
> fria, e acompanha o movimento.

**Blocos 6 e 12 — CTA**
> Ver a linha de neoprene

**Bloco 7 — Frete grátis**
> Frete grátis para todo o Brasil, sem valor mínimo.

**Bloco 8 — Camiseta Cabo Frio**
> Corpo em neoprene Span/Flex de 1,5 mm. Mangas, recortes e gola em poliamida com UV 50+,
> para as sessões longas de sol. E o punho é de neoprene: a manga fica onde você deixou,
> sem escorregar no meio da remada.

**Bloco 9 — Bermuda Joaquina**
> Corpo em neoprene nylon/nylon de 1,5 mm e barra em open cell, que absorve menos água e
> seca mais rápido. O cordão de ajuste fica todo por dentro do cós, e a costura flat não
> atrita na pele.

**Bloco 10 — Sapatilha esportiva**
> Três tecidos numa peça só: solado antiderrapante em neoprene Shak, contorno do pé em
> neoprene de 1,5 mm revestido de nylon nas duas faces, e punho duplo em poliamida.
> Aderência e isolamento térmico onde o piso escorrega.

**Bloco 11 — Fechamento**
> Três peças, o mesmo 1,5 mm de neoprene. É o que mantém a temperatura do corpo e o
> movimento solto, da entrada até a saída da água.

A versão em texto puro da peça está em `04-copy.md` e deve acompanhar o envio.

---

## 4. Hierarquia e intenção

Intenção escrita como resultado a atingir, não como solução visual.

| Bloco | Peso | Intenção |
|---|---|---|
| 3 — Topo | secundário | Identificar o remetente sem competir com o hero. Existem logos para header claro e escuro, então o fundo é decisão sua |
| 4 — Hero | **dominante** | Ser a primeira coisa lida, e comunicar "linha de neoprene" mesmo se a foto não carregar |
| 5 — Argumento | **dominante** | O 1,5 mm precisa ficar na cabeça de quem lê só esta frase |
| 6 — CTA | dominante | Visível sem rolar em tela de celular, junto com o argumento |
| 7 — Frete grátis | apoio | Notado sem esforço, e claramente subordinado ao argumento acima dele |
| 8, 9, 10 — Produtos | apoio | Os três precisam parecer da mesma família, com o mesmo tratamento, e ainda assim dar para distinguir onde um termina e o outro começa |
| 11 — Fechamento | apoio | Reamarrar as três peças no mesmo argumento antes do último clique |
| 12 — CTA final | dominante | Alcançável para quem leu tudo, sem precisar voltar ao topo |
| 13 — Rodapé | secundário | Cumprir a obrigação legal sem roubar atenção |

**O corte de leitura que importa:** quem rola metade da peça e abandona precisa sair
sabendo que a Use Zero Hora lançou uma linha de neoprene de 1,5 mm com três peças, e que
o frete é grátis. Isso cai por volta do bloco 8.

---

## 5. Restrições técnicas de email

- **Corpo de 600 px**, layout em tabela, CSS inline.
- **Imagens hospedadas por URL.** Resolvido: as URLs de produção estão em
  `06-urls-imagens.md`, servidas pelo GitHub raw e **fixadas em commit SHA**. Copie a URL
  inteira, com o SHA. Trocar o SHA por um nome de branch quebra todas as imagens de todos
  os emails já entregues no dia em que a branch for apagada.
- **Texto alternativo em toda imagem**, com o texto da seção 2.1.
- **A peça precisa funcionar sem imagem.** Imagem bloqueada é o estado default da
  primeira abertura em boa parte dos clientes. Se a headline, o argumento, o frete e os
  três produtos só existirem dentro de imagem, a peça chega vazia.
- **Dark mode legível**, sem depender de fundo branco. Os três produtos são pretos, o que
  torna o contorno deles frágil em fundo escuro — é um problema real de composição aqui.
- **Um único destino de clique**, com UTM consistente em todas as ocorrências.

---

## 6. A restrição dominante: 102 KB

O disparo é por Mailmeteor sobre Gmail. **O HTML precisa ficar abaixo de 102 KB.** Acima
disso o Gmail corta a peça no meio e esconde o resto atrás de "ver mensagem inteira" —
e o que fica escondido é o fim do email, onde está o último CTA.

Trabalhe com alvo de **80 KB**. A folga cobre o pixel de rastreio, o rodapé e a reescrita
de link que a ferramenta injeta no envio, depois de o arquivo já estar fechado.

A conta é de HTML e CSS inline; imagem hospedada por URL não entra nela. O que estoura o
limite é CSS repetido bloco a bloco e markup redundante — e esta peça tem **três blocos de
produto de estrutura idêntica**, que é exatamente o padrão que multiplica código. Vale
resolver isso no desenho do markup desde o começo, não no fim por compressão.

Informe o tamanho final do HTML na entrega.

**Mailmeteor, duas consequências:** a personalização usa merge tag por coluna da planilha
do Google Sheets — confirme a sintaxe na conta e deixe todo merge tag com valor de
fallback, para campo vazio não virar buraco no meio da frase. E o link de descadastro é
obrigatório e gerenciado pela ferramenta: reserve o lugar dele no rodapé.

---

## 7. O que é decisão sua

Grid, composição, paleta, tipografia, espaçamento, ritmo visual entre os três produtos,
tratamento visual das features, uso dos assets extras (`camiseta-packshot-costas`,
`bermuda-packshot-lateral`, `sapatilha-packshot-lateral`) e todo o código HTML.

Este documento não opina sobre nada disso. Ele diz o que cada bloco precisa cumprir; como
cumprir é seu trabalho.

---

## 8. O que não é negociável

- **A ordem dos produtos**: camiseta, bermuda, sapatilha. O critério está em
  `02-demanda-keywords.md` — amplitude de uso, na ausência de dado de busca.
- **O CTA único**, mesmo texto e mesmo destino nas duas ocorrências. Os blocos de produto
  não ganham link próprio.
- **A posição do frete grátis**: visível, em bloco próprio, depois do argumento da linha.
  Nunca no assunto, no preheader ou na primeira frase — os dados da marca mostram
  correlação negativa com conversão nessa posição.
- **A ausência de preço e de prazo de entrega.** É decisão editorial da campanha, não
  esquecimento. Não preencha.
- **O texto exato da copy.** Mudança de texto volta para a etapa de copy; não ajuste no
  layout, nem para caber melhor. Se um trecho atrapalhar a composição, aponte o conflito.

---

## 9. Restrições aceitas

Confirmado em 10/08/2026: os três itens abaixo **não existem** e não vão chegar. Não são
pendência, são o terreno. A peça foi desenhada para funcionar sem eles.

**Sem grade de tamanhos.** O email não responde "que tamanho eu compro". A resposta mora
na página do produto, depois do clique — e é mais um motivo para o CTA único levar à
coleção, onde a pessoa encontra a informação no contexto certo. Não invente tabela de
medidas nem faixa de numeração.

**Sem prova social.** Nenhuma avaliação, selo ou depoimento. Quem faz o trabalho de
credibilidade aqui é a especificidade técnica: 1,5 mm, open cell, Neoprene Shak, UV 50+,
costura flat. Número verificável convence de um jeito diferente de depoimento, e é o que
esta peça tem. Não invente selo, estrela nem contador de avaliação.

**Sem paleta da marca em hexadecimal.** A decisão de cor é sua. Três observações para
informar a escolha, sem restringi-la:

- O logo veio **só em preto e branco** — não existe versão colorida no pacote.
- Os três produtos são pretos, e todos os packshots têm fundo claro e neutro.
- As fotos de linha são de fim de tarde, com laranja e dourado na água e na pele. A cor
  quente da peça pode vir das fotos, sem precisar de paleta gráfica.

Uma ressalva importante: a marca **usa cores vibrantes em outras frentes** — é assinatura
dela destacar o surfista no mar. A ausência de paleta aqui significa que não temos o
arquivo, não que a marca seja monocromática. Se você usar uma cor de destaque, ela é
invenção sua, não a cor oficial: aponte isso na entrega, para virar decisão consciente em
vez de precedente acidental.

**Resolvidas:** hospedagem das imagens (`06-urls-imagens.md`) e logo (três variações em
`imagens-design/04-marca/`).

---

## Prompt para colar no Claude Design

```
Você vai desenhar e codificar um email HTML de lançamento para a Use Zero Hora, marca D2C
brasileira de surf e beachwear. A peça lança uma linha de neoprene com três produtos:
camiseta Cabo Frio, bermuda Joaquina e sapatilha esportiva.

O briefing completo — copy final, inventário de imagens com texto alternativo, hierarquia
por bloco e restrições técnicas — está em
ativacao/campanhas/2026-08-lancamento-neoprene/05-brief-design.md.
As imagens estão em imagens-design/, organizadas por produto.

<seu_escopo>
Layout, composição, posicionamento, grid, paleta, tipografia, ritmo visual, tratamento
visual das features e o código HTML são decisões suas. O briefing diz o que cada bloco
precisa cumprir; como ele cumpre é o seu trabalho.
</seu_escopo>

<atencao_as_pastas>
Em imagens-design/<produto>/ estão os assets: fotografia de produto e de uso, que entram
no email. Em imagens-design/<produto>/referencia/ estão infográficos com texto aplicado,
que NÃO entram no email — eles mostram como a marca já comunicou cada feature. O
tratamento visual das features nesta peça é criação sua a partir da copy, não recorte
dessas artes.
</atencao_as_pastas>

<o_que_ja_esta_decidido>
A ordem dos produtos, o texto da copy, o CTA único, a posição do frete grátis e a
ausência de preço e prazo de entrega estão fechados. Se algum deles atrapalhar o layout
que você quer fazer, aponte o conflito em vez de resolvê-lo por conta própria.
</o_que_ja_esta_decidido>

<restricao_dominante>
O disparo é por Mailmeteor sobre Gmail: o HTML precisa ficar abaixo de 102 KB, senão o
Gmail corta a peça no meio e esconde o último CTA. Trabalhe com alvo de 80 KB — a folga
cobre o pixel de rastreio e a reescrita de link que a ferramenta injeta no envio.

A conta é de HTML e CSS inline; imagem hospedada por URL não entra nela. Os três blocos
de produto têm estrutura idêntica, que é o padrão que multiplica CSS — vale resolver isso
no desenho do markup, não no fim por compressão. Informe o tamanho final do HTML.
</restricao_dominante>

<restricoes_de_email>
- Corpo de 600 px, layout em tabela, CSS inline
- Imagens por URL, com texto alternativo em todas
- A mensagem central chega mesmo com imagem bloqueada
- Dark mode legível: os três produtos são pretos, e o contorno deles some em fundo escuro
- Um único destino de clique, com UTM consistente
- Merge tags com valor de fallback e lugar reservado para o link de descadastro
</restricoes_de_email>

Entregue o layout e o HTML. Aponte, ao final, qualquer ponto do briefing que tenha
conflitado com uma decisão visual.
```
