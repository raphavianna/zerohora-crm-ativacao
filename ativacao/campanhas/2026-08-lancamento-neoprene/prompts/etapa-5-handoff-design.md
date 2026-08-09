# Etapa 5 — Pacote de handoff para o Claude Design

**Entra:** `01-fichas-produto.md` + `03-arquitetura-email.md` + `04-copy.md` + as imagens.
**Sai:** `05-brief-design.md` — o documento que vai para o Claude Design.

Esta é **a fronteira do projeto**. Daqui sai o *quê* e o *porquê*; do Claude Design vem o
*como parece* e o código. O produto desta etapa é um documento único, autossuficiente,
que alguém sem acesso a esta conversa consegue executar.

O prompt abaixo tem duas partes. A **parte 1** monta o pacote. A **parte 2** é o texto
que você cola no Claude Design.

---

## A1) PROMPT — montar o pacote

```
Monte o pacote de handoff do email de lançamento da linha de neoprene para o Claude
Design. Esta é a Etapa 5: você não escreve HTML, não escolhe cor, fonte, grid nem
espaçamento, e não decide composição. Você entrega a especificação que torna essas
decisões possíveis.

<copy>
{{COPY}}
</copy>

<arquitetura>
{{ARQUITETURA}}
</arquitetura>

<fichas>
{{FICHAS_PRODUTO}}
</fichas>

<tarefa>
Produza 05-brief-design.md, autossuficiente, com estas sete seções:

1. **O trabalho** — a peça em cinco linhas: o que é, para quem vai, o que precisa
   acontecer depois da leitura, e o que faria a peça falhar.

2. **Inventário de imagens** — uma tabela com toda imagem que a peça usa: caminho exato
   em imagens-design/, o bloco onde entra, a função dela ali, o texto alternativo já
   escrito na Etapa 4 e se ela é foto de produto, infográfico ou elemento de marca.
   Caminho errado no inventário é o defeito mais caro deste documento, porque só aparece
   no fim. Confira cada um contra o que existe em disco.

3. **Copy por bloco, pronta para colar** — o texto final, na ordem, identificado pelo
   bloco. Sem comentário editorial no meio; comentário vai em nota apartada.

4. **Hierarquia e intenção** — por bloco, o peso (dominante, apoio, secundário) e a
   intenção que ele precisa cumprir. Escreva a intenção como resultado a atingir, não
   como solução visual: "este bloco precisa ser a primeira coisa lida, mesmo sem imagem"
   em vez de "título 32 px centralizado".

5. **Restrições técnicas de email** — as que limitam o layout, com o motivo de cada uma:
   corpo de 600 px; assets em 1200 px de largura para tela retina; a peça precisa
   comunicar a mensagem central com imagem bloqueada; texto alternativo obrigatório em
   toda imagem; um único destino de clique; a peça é lida em dark mode por parte da
   base; alvo de peso total abaixo de 1 MB para não ser cortada pelo Gmail.

6. **O que é decisão do Design** — declare explicitamente: grid, composição, paleta,
   tipografia, espaçamento, tratamento dos infográficos, ritmo visual entre os três
   produtos e o código do email. Este documento não opina sobre nada disso.

7. **O que não é negociável** — a ordem dos produtos e a justificativa de demanda por
   trás dela; o call-to-action único; o frete grátis visível e fora da posição de gancho;
   o texto exato da copy, cuja mudança volta para a Etapa 4 em vez de ser ajustada no
   layout.
</tarefa>

Antes de montar, raciocine em <thinking>: percorra o inventário de imagens e confirme que
todo arquivo citado existe em disco no caminho escrito, e que toda imagem marcada como
infográfico na Etapa 1 aparece no inventário. Arquivo ausente vira linha na seção de
pendências, com o pedido de arte correspondente.
```

---

## A2) PROMPT — o texto para colar no Claude Design

```
Você vai desenhar e codificar um email HTML de lançamento para a Use Zero Hora, marca D2C
brasileira de surf e beachwear.

O briefing completo — copy final, inventário de imagens, hierarquia por bloco e
restrições técnicas — está em 05-brief-design.md, e as imagens estão em imagens-design/,
organizadas por produto.

<seu_escopo>
Layout, composição, posicionamento, grid, paleta, tipografia, ritmo visual e o código
HTML do email são decisões suas. O briefing diz o que cada bloco precisa cumprir; como
ele cumpre é o seu trabalho.
</seu_escopo>

<o_que_ja_esta_decidido>
A ordem dos produtos, o texto da copy, o call-to-action único e a posição do frete grátis
vieram de dados e estão fechados. Se algum deles atrapalhar o layout que você quer fazer,
aponte o conflito em vez de resolvê-lo por conta própria — a decisão volta para quem
escreveu a copy.
</o_que_ja_esta_decidido>

<restricoes_de_email>
Email não é página. O código precisa sobreviver a cliente antigo e a renderização
hostil:
- Corpo de 600 px, layout em tabela, CSS inline
- Imagens em 1200 px de largura, servidas em 600 px, com texto alternativo em todas
- A mensagem central chega mesmo com imagem bloqueada
- Dark mode legível, sem depender de fundo branco
- Um único destino de clique
- Peso total abaixo de 1 MB, para o Gmail não cortar a peça
</restricoes_de_email>

Entregue o layout e o HTML. Aponte, ao final, qualquer ponto do briefing que tenha
conflitado com uma decisão visual.
```

---

## B) RACIONAL TÉCNICO

- **O pacote é autossuficiente por exigência explícita.** Handoff que depende do
  histórico da conversa quebra no momento em que troca de janela — que é exatamente o que
  acontece aqui.
- **Seções 6 e 7 são o coração do documento**: uma declara o que o Design decide, a outra
  o que não se toca. Sem esse par, o handoff vira ou uma camisa de força (o briefing
  descreve pixel) ou um vale-tudo (o layout reescreve a copy). As duas falhas são comuns
  e as duas custam uma volta inteira.
- **Intenção como resultado, não como solução visual** ("precisa ser a primeira coisa
  lida" em vez de "32 px centralizado"): é a formulação que preserva a inteligência do
  Design em vez de reduzi-lo a executor, que foi o pedido.
- **Verificação de caminho de arquivo no `<thinking>`**: o inventário de imagens é o
  ponto de falha silenciosa do handoff, porque caminho errado só aparece quando o Design
  tenta usar o arquivo, já do outro lado da fronteira.
- **A2 repete as restrições de email** em vez de referenciar o briefing. Redundância
  proposital: essas seis linhas são o que separa um email que renderiza de um que quebra
  no Outlook, e elas precisam estar na primeira tela do prompt que o Design recebe.
- **"Aponte o conflito em vez de resolvê-lo"** dá ao Design uma saída legítima quando a
  copy atrapalha o layout, no lugar da saída default, que é reescrever a copy no meio do
  HTML e ninguém perceber.

## C) VARIÁVEIS

| Variável | O que recebe |
|---|---|
| `{{COPY}}` | Conteúdo de `04-copy.md` |
| `{{ARQUITETURA}}` | Conteúdo de `03-arquitetura-email.md` |
| `{{FICHAS_PRODUTO}}` | Conteúdo de `01-fichas-produto.md` |

## E) COMO TESTAR

Sucesso: entregue o `05-brief-design.md` a alguém que não acompanhou o projeto e peça que
descreva a peça. Se a descrição bater com a intenção, o handoff está pronto.

Caso de teste: confira cada caminho do inventário de imagens contra o disco. Um caminho
quebrado invalida o pacote — é a falha que só aparece do outro lado da fronteira, quando
corrigir já custa uma volta inteira.
