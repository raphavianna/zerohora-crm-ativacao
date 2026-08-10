# 04 — Marca

## Os três logos disponíveis

| Arquivo | O que é | Dimensão | Peso | Funciona sobre |
|---|---|---|---|---|
| `logo-use-zero-hora-branco.png` | Negativo: símbolo "Z" + lettering "USE ZERO HORA", branco, fundo transparente | 1694 × 788 | 29 KB | só fundo escuro |
| `logo-use-zero-hora-preto.png` | Positivo: mesma composição, em preto, fundo transparente | 1694 × 788 | 31 KB | só fundo claro |
| `logo-use-zero-hora-redondo.png` | Só o símbolo "Z" em preto dentro de um disco branco, fundo transparente fora do disco | 500 × 500 | 11 KB | **claro e escuro** |

Todos com canal alfa real e antisserrilhado (o redondo tem 115 níveis de alfa, não
transparência binária — a borda do disco fica lisa em qualquer tamanho).

## Qual usar no email

**Recomendado: `logo-use-zero-hora-branco.png` sobre header escuro.**

Dois motivos. Primeiro, ele traz o nome da marca por extenso — o símbolo sozinho não diz
"Use Zero Hora" para quem ainda não conhece a marca. Segundo, e mais técnico: o dark mode
do Gmail costuma escurecer fundo claro e deixar fundo já escuro em paz. Um header escuro
com logo branco é o arranjo que menos depende de como o cliente de email decide tratar as
cores.

**Alternativa segura: `logo-use-zero-hora-redondo.png`.** Ele carrega o próprio disco
branco, então é legível sobre qualquer fundo, aconteça o que acontecer com o dark mode.
O preço é perder o lettering. Vale se o Design quiser header claro, ou se quiser um logo
pequeno e discreto no topo.

**`logo-use-zero-hora-preto.png`** serve para header claro, com a ressalva do dark mode
acima: se o cliente escurecer o fundo do bloco, o logo preto some.

Em qualquer um dos três, o texto alternativo é `Use Zero Hora` — assim a marca chega
mesmo com imagem bloqueada.

## O que ficou de fora do repositório

O pacote recebido em 10/08/2026 trazia também:

- **Vetores** (`.ai`, `.eps`, `.pdf`), versões Digital e Print, positivo e negativo,
  somando cerca de 8,5 MB. São os masters da marca e não servem para email — nenhum
  cliente de email renderiza vetor. Ficaram fora para não inflar o repositório. Se a
  intenção for usar este repo como arquivo de marca, vale trazê-los num commit próprio.
- **`logopretouzh.jpeg`** — o símbolo branco sobre um quadrado preto sólido, em JPEG.
  Deixado de fora de propósito: JPEG não tem transparência, então ele carrega o quadrado
  preto para dentro de qualquer layout, e a compressão JPEG suja as bordas duras do
  símbolo. Os PNGs acima resolvem o mesmo caso sem esses dois defeitos.

## O que ainda falta

Paleta em hexadecimal, tipografia e selos.

## Padrão de nome

`logo-<variação>.png` para logo, `selo-<nome>.png` para selo. Sempre PNG com fundo
transparente.
