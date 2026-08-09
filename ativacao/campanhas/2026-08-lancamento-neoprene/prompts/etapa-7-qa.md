# Etapa 7 — QA do email entregue pelo Design

**Entra:** o HTML que o Claude Design produziu + `04-copy.md` + `05-brief-design.md`.
**Sai:** `07-qa-disparo.md`.

Roda **depois** do Design. Confere se a peça entregue cumpre a especificação e se
sobrevive ao mundo real das caixas de entrada. Não reescreve layout nem código: aponta.

---

## A) PROMPT

```
Faça o QA do email de lançamento da linha de neoprene que o Claude Design entregou,
contra a copy aprovada e o briefing.

<html_entregue>
{{HTML}}
</html_entregue>

<copy_aprovada>
{{COPY}}
</copy_aprovada>

<briefing>
{{BRIEF_DESIGN}}
</briefing>

<verificacoes>
Percorra as sete verificações abaixo. Cada uma fecha em passou ou falhou, com a evidência
do arquivo ao lado. Verificação sem evidência citada conta como não feita.

1. **Fidelidade da copy** — o texto do HTML é idêntico ao de 04-copy.md, palavra por
   palavra. Qualquer divergência é apontada com as duas versões lado a lado, ainda que
   pareça melhoria: mudança de copy volta para a Etapa 4, não entra pelo layout.

2. **Limites** — assunto até 50 caracteres e sem emoji; preheader até 90; primeira frase
   do corpo entre 15 e 25 palavras. Conte e mostre a contagem.

3. **Posição do frete grátis** — ausente do assunto, do preheader e da primeira frase;
   presente e visível no corpo.

4. **Imagens** — toda imagem tem texto alternativo que carrega a informação, não a
   aparência; toda `src` aponta para arquivo que existe; largura de origem compatível
   com tela retina.

5. **Peça sem imagem** — leia o HTML ignorando toda imagem e reproduza o que sobra. A
   mensagem central precisa chegar. Escreva o que sobrou, para o julgamento ser feito
   sobre o texto e não sobre a impressão.

6. **Clique** — um único destino, apontando para usezerohora.com.br, com UTM
   consistente em todas as ocorrências. Liste toda `href` encontrada.

7. **Robustez de cliente** — layout em tabela, CSS inline, peso total abaixo de 1 MB,
   legibilidade em dark mode, link de descadastro presente.
</verificacoes>

<severidade>
Classifique cada achado:
- **Bloqueia o disparo** — copy divergente, limite estourado, link quebrado, ausência de
  descadastro, peça ilegível sem imagem.
- **Corrige antes** — alt fraco, UTM inconsistente, peso alto, risco em dark mode.
- **Registra** — o que funciona mas vale melhorar no próximo disparo.

Ordene o relatório por severidade. Não misture os três níveis na mesma lista: quem lê
precisa saber em dez segundos se pode disparar.
</severidade>

Se uma verificação não puder ser feita com o que está no contexto — peso do arquivo, por
exemplo, sem acesso aos assets — declare "não verificável aqui" e diga o que seria
preciso. Não estime.

Produza 07-qa-disparo.md com o relatório por severidade e, no fim, um veredito único:
libera o disparo, ou não libera e por quê.
```

---

## B) RACIONAL TÉCNICO

- **Checklist binário com evidência obrigatória**: QA sem citação vira opinião, e opinião
  não bloqueia disparo. "Verificação sem evidência conta como não feita" fecha a brecha.
- **A verificação 5 pede que o modelo escreva o que sobra** em vez de julgar se sobra o
  suficiente. Produzir o texto força a leitura real; julgar direto convida ao "sim,
  comunica bem".
- **Fidelidade de copy como verificação 1, com a regra de que melhoria também é
  divergência.** É o vazamento mais comum entre design e conteúdo, e o mais difícil de
  detectar depois, porque a versão nova costuma soar bem.
- **Três níveis de severidade, listados separadamente.** Relatório de QA é lido sob
  pressão de prazo; se o achado que bloqueia estiver na décima linha de uma lista única,
  ele é disparado junto com a peça.
- **"Não verificável aqui"** é a saída anti-alucinação (Cap. 8) para o QA — sem ela, o
  modelo estima peso de arquivo e legibilidade em dark mode sem ter visto nenhum dos dois.
- **Veredito único no fim**: o documento precisa terminar em decisão, não em lista.

## C) VARIÁVEIS

| Variável | O que recebe |
|---|---|
| `{{HTML}}` | O HTML entregue pelo Claude Design |
| `{{COPY}}` | Conteúdo de `04-copy.md` |
| `{{BRIEF_DESIGN}}` | Conteúdo de `05-brief-design.md` |

## E) COMO TESTAR

Sucesso: rode o QA sobre uma versão do HTML em que você trocou uma palavra da copy de
propósito. A verificação 1 precisa pegar a troca e classificá-la como bloqueio.

Segundo teste: remova o `alt` de uma imagem. A verificação 4 precisa pegar, e a 5 precisa
mostrar o buraco que isso abre na peça sem imagem.
