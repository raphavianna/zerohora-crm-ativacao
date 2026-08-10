# Prompt para o Claude Design — autossuficiente

O Claude Design não tem acesso a este repositório. Por isso este prompt carrega **tudo**
dentro dele: URLs completas das imagens, copy final, restrições e limites. É só copiar o
bloco inteiro e colar.

Se qualquer imagem for trocada ou adicionada, o SHA muda e as URLs precisam ser regeradas
a partir de `06-urls-imagens.md` antes de usar este prompt de novo.

---

```
Você vai desenhar e codificar um email HTML de lançamento para a Use Zero Hora, marca
D2C brasileira de surf e beachwear (usezerohora.com.br). A peça lança uma linha de
neoprene com três produtos: camiseta Cabo Frio, bermuda Joaquina e sapatilha esportiva.

<o_trabalho>
Vai para a base masculina do site próprio, disparada por Mailmeteor sobre Gmail.
O objetivo é venda: o sucesso da peça é clique na coleção de neoprene, não abertura.

O argumento que sustenta tudo: os três produtos compartilham neoprene de 1,5 mm. É o que
transforma três lançamentos soltos em um lançamento de linha, e é o que a peça precisa
deixar na cabeça de quem lê.

O que faria a peça falhar: ser cortada pelo Gmail antes do fim; chegar vazia para quem lê
com imagem bloqueada; ou perder o 1,5 mm em meio a três produtos disputando atenção.
</o_trabalho>

<seu_escopo>
Layout, composição, posicionamento, grid, paleta, tipografia, ritmo visual, tratamento
visual das features e o código HTML são decisões suas. O briefing diz o que cada bloco
precisa cumprir; como ele cumpre é o seu trabalho.
</seu_escopo>

<imagens>
Todas hospedadas e testadas: respondem 200 com content-type de imagem. Use as URLs
exatamente como estão, inclusive o hash longo no meio — ele é o que garante que a imagem
não suma da caixa de entrada de quem já recebeu o email.

LOGO — três variações, escolha uma para o bloco de topo.
Alt em todas: "Use Zero Hora"

Branco, com lettering. Recomendado. Exige fundo escuro no bloco.
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/04-marca/logo-use-zero-hora-branco.png

Redondo, símbolo dentro de disco branco próprio. Legível sobre qualquer fundo. Sem lettering.
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/04-marca/logo-use-zero-hora-redondo.png

Preto, com lettering. Exige fundo claro no bloco.
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/04-marca/logo-use-zero-hora-preto.png

HERO — bloco 4. Horizontal, 1200 × 755. A espuma à esquerda é área livre para a headline.
Alt: "Surfista saindo do mar de camiseta de neoprene de manga longa e bermuda de neoprene, com a prancha debaixo do braço"
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/00-linha-neoprene/linha-hero-surfista-01.jpg

CAMISETA — bloco 8.
Alt: "Camiseta de neoprene Cabo Frio de frente, manga longa e gola alta, na cor preta"
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/01-camiseta-neoprene-cabo-frio/camiseta-packshot-frente.jpg

BERMUDA — bloco 9.
Alt: "Bermuda de neoprene Joaquina vestida, comprimento acima do joelho, na cor preta"
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/02-bermuda-neoprene-joaquina/bermuda-lifestyle-01.jpg

SAPATILHA — bloco 10. O solado é o argumento da peça, por isso é ele que aparece.
Alt: "Solado da sapatilha de neoprene visto de baixo, com a textura antiderrapante cobrindo toda a base"
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/03-sapatilha-esportiva-neoprene/sapatilha-packshot-solado.jpg

FECHAMENTO — bloco 11. É a única foto que mostra as três peças juntas, sapatilhas nos pés.
Alt: "Surfista de costas na beira do mar usando a linha completa: camiseta de neoprene de manga longa, bermuda e sapatilhas nos pés"
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/00-linha-neoprene/linha-lifestyle-praia-01.jpg

DISPONÍVEIS, use onde a composição pedir:
Vertical de corpo inteiro, mesma sessão do hero — alt: "Surfista de corpo inteiro na beira do mar, de camiseta de neoprene de manga longa e bermuda de neoprene"
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/00-linha-neoprene/linha-lifestyle-surfista-02.jpg
Camiseta de costas — alt: "Camiseta de neoprene Cabo Frio de costas, com recorte raglã e costura central"
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/01-camiseta-neoprene-cabo-frio/camiseta-packshot-costas.jpg
Bermuda em detalhe lateral — alt: "Detalhe lateral da bermuda de neoprene Joaquina, com a etiqueta emborrachada junto à barra"
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/02-bermuda-neoprene-joaquina/bermuda-packshot-lateral.jpg
Sapatilha de perfil — alt: "Sapatilha de neoprene de perfil, com cano na altura do tornozelo"
https://raw.githubusercontent.com/raphavianna/zerohora-crm-ativacao/089cbe5dde2521ae712a3897d79d50e618098f2f/imagens-design/03-sapatilha-esportiva-neoprene/sapatilha-packshot-lateral.jpg

Uma restrição sobre as fotos de linha: o texto de marca aplicado nas peças está
embaralhado nelas — o selo circular no peito tem letras ilegíveis, a etiqueta na coxa é
um borrão. Na largura do email o selo fica com cerca de 30 px e lê como selo. Não amplie
nem recorte o peito ou a etiqueta da coxa; é só ali que o defeito aparece.
</imagens>

<copy>
Use este texto exatamente como está. Ele foi escrito contra regras de conversão da marca
e cada número vem da ficha técnica do produto.

ASSUNTO — duas variações para teste A/B:
A: O frio da água não encurta mais a sessão
B: Chegou a linha de neoprene 1,5 mm

PREHEADER — duas variações:
A: Camiseta, bermuda e sapatilha em 1,5 mm. Feitas para água fria, vento e sol forte.
B: Camiseta Cabo Frio, bermuda Joaquina e sapatilha esportiva. As três em neoprene.

BLOCO 3 — Topo: logo.

BLOCO 4 — Hero
Headline: A linha de neoprene chegou
Apoio: Camiseta, bermuda e sapatilha. As três em 1,5 mm.

BLOCO 5 — Argumento da linha
Neoprene de 1,5 mm nas três peças: segura o calor do corpo contra o vento e a água fria,
e acompanha o movimento.

BLOCO 6 — CTA
Ver a linha de neoprene

BLOCO 7 — Frete grátis
Frete grátis para todo o Brasil, sem valor mínimo.

BLOCO 8 — Camiseta Cabo Frio
Corpo em neoprene Span/Flex de 1,5 mm. Mangas, recortes e gola em poliamida com UV 50+,
para as sessões longas de sol. E o punho é de neoprene: a manga fica onde você deixou,
sem escorregar no meio da remada.

BLOCO 9 — Bermuda Joaquina
Corpo em neoprene nylon/nylon de 1,5 mm e barra em open cell, que absorve menos água e
seca mais rápido. O cordão de ajuste fica todo por dentro do cós, e a costura flat não
atrita na pele.

BLOCO 10 — Sapatilha esportiva
Três tecidos numa peça só: solado antiderrapante em neoprene Shak, contorno do pé em
neoprene de 1,5 mm revestido de nylon nas duas faces, e punho duplo em poliamida.
Aderência e isolamento térmico onde o piso escorrega.

BLOCO 11 — Fechamento
Três peças, o mesmo 1,5 mm de neoprene. É o que mantém a temperatura do corpo e o
movimento solto, da entrada até a saída da água.

BLOCO 12 — CTA final: mesmo texto e mesmo destino do bloco 6.

BLOCO 13 — Rodapé: marca e link de descadastro.
</copy>

<hierarquia>
A intenção de cada bloco, escrita como resultado a atingir, não como solução visual:

Bloco 3, topo — secundário. Identificar o remetente sem competir com o hero.
Bloco 4, hero — DOMINANTE. Ser a primeira coisa lida, e comunicar "linha de neoprene"
mesmo se a foto não carregar.
Bloco 5, argumento — DOMINANTE. O 1,5 mm precisa ficar na cabeça de quem lê só esta frase.
Bloco 6, CTA — dominante. Visível sem rolar em tela de celular, junto do argumento.
Bloco 7, frete — apoio. Notado sem esforço e claramente subordinado ao argumento acima dele.
Blocos 8, 9, 10, produtos — apoio. Precisam parecer da mesma família, com o mesmo
tratamento, e ainda assim dar para ver onde um termina e o outro começa.
Bloco 11, fechamento — apoio. Reamarrar as três peças antes do último clique.
Bloco 12, CTA final — dominante. Alcançável para quem leu tudo, sem voltar ao topo.
Bloco 13, rodapé — secundário.

O corte de leitura que importa: quem rola metade da peça e abandona precisa sair sabendo
que a Use Zero Hora lançou uma linha de neoprene de 1,5 mm com três peças, e que o frete
é grátis. Isso cai por volta do bloco 8.
</hierarquia>

<restricao_dominante>
O disparo é por Mailmeteor sobre Gmail: o HTML precisa ficar ABAIXO DE 102 KB. Acima
disso o Gmail corta a peça no meio e esconde o resto atrás de "ver mensagem inteira" — e
o que fica escondido é o fim do email, onde está o último CTA.

Trabalhe com alvo de 80 KB. A folga cobre o pixel de rastreio e a reescrita de link que a
ferramenta injeta no envio, depois de o arquivo já estar fechado.

A conta é de HTML e CSS inline; imagem hospedada por URL não entra nela. O que estoura o
limite é CSS repetido bloco a bloco e markup redundante — e esta peça tem três blocos de
produto de estrutura parecida, que é justamente o padrão que multiplica código. Vale
resolver isso no desenho do markup desde o começo, não no fim por compressão.

Informe o tamanho final do HTML na entrega.
</restricao_dominante>

<restricoes_de_email>
- Corpo de 600 px, layout em tabela, CSS inline
- Texto alternativo em todas as imagens, usando os alts acima
- A mensagem central chega mesmo com imagem bloqueada. Se headline, argumento, frete e os
  três produtos só existirem dentro de imagem, a peça chega vazia
- Dark mode legível. Atenção: os três produtos são pretos, e o contorno deles fica frágil
  em fundo escuro
- Um único destino de clique, com UTM consistente em todas as ocorrências
- Merge tags do Mailmeteor com valor de fallback, para campo vazio não virar buraco no
  meio da frase. Reserve o lugar do link de descadastro no rodapé
</restricoes_de_email>

<nao_negociavel>
- A ordem dos produtos: camiseta, bermuda, sapatilha.
- O CTA único: mesmo texto e mesmo destino nas duas ocorrências, sempre para a coleção de
  neoprene. Os blocos de produto NÃO ganham link próprio.
- A posição do frete grátis: visível, em bloco próprio, depois do argumento da linha.
  Nunca no assunto, no preheader ou na primeira frase — os dados da marca mostram
  correlação negativa com conversão nessa posição.
- O texto exato da copy. Mudança de texto volta para quem escreveu; não ajuste no layout,
  nem para caber melhor. Se um trecho atrapalhar a composição, aponte o conflito.
</nao_negociavel>

<ausencias_deliberadas>
Estes itens não existem na peça de propósito. Não preencha nenhum deles:

- Sem preço. Decisão editorial: o preço aparece na página do produto, depois do clique.
- Sem prazo de entrega.
- Sem tabela de medidas e sem grade de numeração. O dado não existe, e a resposta mora na
  página do produto. Nenhum elemento pode sugerir que a informação está no email.
- Sem prova social. Não invente selo, estrela, contador de avaliação nem depoimento. A
  credibilidade da peça vem da especificidade técnica: 1,5 mm, open cell, Neoprene Shak,
  UV 50+, costura flat.
</ausencias_deliberadas>

<sobre_cor>
Não existe paleta da marca em hexadecimal disponível. A decisão de cor é sua. Três
observações para informar a escolha:
- O logo veio só em preto e branco; não há versão colorida.
- Os três produtos são pretos, e os packshots têm fundo claro e neutro.
- As fotos de linha são de fim de tarde, com laranja e dourado na água e na pele. A cor
  quente da peça pode vir da fotografia, sem paleta gráfica nenhuma.

Uma ressalva: a marca usa cores vibrantes em outras frentes — é assinatura dela destacar
o surfista no mar. A ausência de paleta aqui significa que o arquivo não está disponível,
não que a marca seja monocromática. Se você usar uma cor de destaque, ela é invenção sua
e não a cor oficial: aponte isso na entrega.
</sobre_cor>

Entregue o layout e o HTML completo. No fim, informe o tamanho do HTML em KB e aponte
qualquer ponto do briefing que tenha conflitado com uma decisão visual sua.
```
