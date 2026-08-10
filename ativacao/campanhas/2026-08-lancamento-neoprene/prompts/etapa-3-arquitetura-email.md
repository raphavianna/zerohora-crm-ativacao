# Etapa 3 — Arquitetura do email

**Entra:** `01-fichas-produto.md` + `02-demanda-keywords.md`.
**Sai:** `03-arquitetura-email.md`.

Define **quais blocos existem, em que ordem e por quê**. Não define aparência: nada de
cor, fonte, espaçamento ou grid — isso é do Claude Design.

---

## A) PROMPT

```
Defina a arquitetura de conteúdo do email de lançamento da linha de neoprene. Esta é a
Etapa 3: nenhuma copy final é escrita aqui, e nenhuma decisão visual é tomada aqui.

<fichas>
{{FICHAS_PRODUTO}}
</fichas>

<demanda>
{{DEMANDA_KEYWORDS}}
</demanda>

<tarefa>
Produza a lista ordenada de blocos do email. Para cada bloco, defina cinco coisas e só
elas:

1. **Função** — o trabalho que este bloco faz para levar à compra. Um bloco sem função
   declarada sai da peça.
2. **Conteúdo** — que informação entra, referenciada às fichas. Sem escrever a copy
   final; a Etapa 4 faz isso.
3. **Imagens** — quais arquivos de imagens-design/ este bloco usa, por caminho exato.
4. **Peso na hierarquia** — dominante, de apoio ou secundário. É a instrução que o
   Claude Design vai traduzir em tamanho e posição.
5. **Comportamento com imagem bloqueada** — o que a pessoa entende deste bloco se
   nenhuma imagem carregar.
</tarefa>

<restricoes_da_peca>
- Um único call-to-action, direto para usezerohora.com.br. Ele pode se repetir
  fisicamente ao longo da peça, mas é sempre a mesma ação e o mesmo destino.
- Os três produtos aparecem, na ordem que a Decisão 1 da Etapa 2 estabeleceu.
- O frete grátis tem bloco próprio, visível, posicionado depois do primeiro argumento de
  produto. Ele não abre a peça e não é o mote.
- As únicas imagens disponíveis são as que a Etapa 1 classificou como **asset**
  (fotografia de produto e de uso). Os infográficos existentes são referência de conteúdo
  e não entram na peça: onde a arquitetura pedir destaque de feature, o bloco descreve a
  informação a destacar, e o tratamento visual dela é criado pelo Claude Design.
- A peça não cita preço nem prazo de entrega. Nenhum bloco existe para isso.
- A dobra inicial precisa comunicar lançamento de linha de neoprene mesmo sem imagem
  carregada.
</restricoes_da_peca>

<hierarquia>
Ordene os blocos por uma decisão explícita de hierarquia, não por convenção de template.
Declare qual bloco domina a dobra e por quê, e o que a pessoa que rola metade da peça e
abandona precisa ter absorvido até ali.

Trate a peça como tendo três leitores simultâneos, e diga como a arquitetura serve cada
um: quem lê só o assunto e o preheader; quem abre, olha e rola até o meio; quem lê tudo.
</hierarquia>

Antes de listar os blocos, raciocine em <thinking> sobre a tensão central desta peça: é
um lançamento de linha com três produtos, e cada produto compete por atenção com os
outros dois. Decida se a peça vende a linha e depois as peças, ou vende a peça de maior
demanda e usa as outras duas como complemento. Justifique com o dado da Etapa 2.

Produza 03-arquitetura-email.md com:
1. A decisão de estratégia da peça (linha primeiro × produto-âncora primeiro), com
   justificativa numérica
2. A tabela de blocos: ordem, nome, função, conteúdo, imagens, peso, comportamento sem
   imagem
3. O wireframe verbal — a peça descrita de cima para baixo em prosa corrida, do jeito que
   alguém que não pode ver a tela entenderia a sequência
4. O que ficou de fora e por quê
```

---

## B) RACIONAL TÉCNICO

- **Cinco campos fixos por bloco**, com "função" em primeiro: bloco sem função é o
  entulho clássico de email de lançamento (o "sobre a marca" que ninguém lê).
- **"Peso na hierarquia" em vez de tamanho em pixel**: é a tradução exata da fronteira
  com o Design. Aqui se diz *o que precisa dominar*; lá se decide *como dominar*.
- **Comportamento com imagem bloqueada como campo obrigatório** por bloco, não como nota
  de rodapé. Em email, imagem bloqueada é o estado default da primeira abertura em boa
  parte dos clientes, e uma peça de lançamento que só existe em imagem chega vazia.
- **Os três leitores simultâneos** forçam a arquitetura a ser testada contra o
  comportamento real de leitura, em vez de otimizar só para quem lê tudo — que é a
  minoria.
- **Precognition sobre a tensão da peça** (Cap. 6): três produtos competindo por atenção
  é o problema de verdade desta arquitetura. Nomear a tensão no `<thinking>` evita a saída
  preguiçosa de três blocos idênticos em sequência, que não hierarquiza nada.
- **"O que ficou de fora e por quê"**: torna a omissão auditável e evita a volta seguinte
  em que alguém pergunta por que o tal bloco sumiu.

## C) VARIÁVEIS

| Variável | O que recebe |
|---|---|
| `{{FICHAS_PRODUTO}}` | Conteúdo de `01-fichas-produto.md` |
| `{{DEMANDA_KEYWORDS}}` | Conteúdo de `02-demanda-keywords.md`, ou a nota de dado indisponível |

## E) COMO TESTAR

Sucesso: o wireframe verbal é compreensível para alguém que nunca viu as artes, e cada
bloco declara o que sobra dele sem imagem.

Caso de teste: leia só a coluna "comportamento com imagem bloqueada", de cima para baixo.
Se essa leitura sozinha não comunicar "a Use Zero Hora lançou uma linha de neoprene com
três peças e o frete é grátis", a arquitetura depende demais de imagem e precisa voltar.
