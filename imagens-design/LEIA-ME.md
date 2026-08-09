# imagens-design — artes de origem das campanhas de CRM

Aqui ficam **as artes originais** (as peças que o design já produziu) e os **recortes
prontos para o email**. Esta pasta é a **fonte de verdade visual**: toda informação de
produto que entrar na copy do email precisa existir aqui ou na página do produto.

> Regra herdada do projeto: anúncio e email só prometem o que a arte ou a página do
> produto sustentam. Nada de benefício inventado.

## Como subir uma arte

1. Escolha a pasta do produto (ou `00-linha-neoprene` se a arte fala da linha inteira).
2. Suba o arquivo com o nome no padrão abaixo.
3. Não precisa criar subpasta — o nome do arquivo já carrega o tipo.

## Padrão de nome

```
<produto>-<tipo>-<nn>.<ext>
```

| Campo | Valores | Exemplo |
|---|---|---|
| `produto` | `camiseta`, `bermuda`, `sapatilha`, `linha` | `bermuda` |
| `tipo` | `arte` (peça completa), `packshot` (produto recortado), `infografico`, `medidas`, `detalhe` (costura, zíper, tecido), `lifestyle` (uso real), `selo` | `infografico` |
| `nn` | sequencial de 2 dígitos | `01` |

Exemplos válidos:

```
imagens-design/02-bermuda-neoprene-joaquina/bermuda-arte-01.jpg
imagens-design/02-bermuda-neoprene-joaquina/bermuda-infografico-01.png
imagens-design/00-linha-neoprene/linha-medidas-01.png
imagens-design/04-marca/logo-horizontal.png
```

## Formatos

- **Artes de referência (leitura)**: JPG ou PNG, qualquer resolução. É delas que a copy
  extrai claim, medida, tecnologia e número.
- **Assets do email (produção)**: PNG ou JPG **com largura de 1200 px** (2× do corpo de
  600 px), para render nítido em tela retina.
- Sem PDF e sem arquivo de editor (`.ai`, `.psd`) — o email não os usa e eles pesam o repo.

## Pastas

| Pasta | Conteúdo |
|---|---|
| `00-linha-neoprene/` | Artes da linha como um todo: hero de lançamento, banner, infográfico da tecnologia do neoprene, tabela de medidas comum |
| `01-camiseta-neoprene-cabo-frio/` | Camiseta de neoprene Cabo Frio |
| `02-bermuda-neoprene-joaquina/` | Bermuda de neoprene Joaquina |
| `03-sapatilha-esportiva-neoprene/` | Sapatilha esportiva de neoprene |
| `04-marca/` | Logo, paleta, tipografia, selos e ícones reutilizáveis entre campanhas |

## O que acontece depois do upload

Cada arte é lida e vira uma **ficha de produto** em
`ativacao/campanhas/<campanha>/01-fichas-produto.md`: claim, tecnologia, medida, cor,
preço (com data da coleta) e quais **infográficos** merecem sobreviver no email em vez de
virar texto corrido.
