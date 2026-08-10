# imagens-design — artes de origem das campanhas de CRM

Aqui ficam **as artes originais** (as peças que o design já produziu) e os **recortes
prontos para o email**. Esta pasta é a **fonte de verdade visual**: toda informação de
produto que entrar na copy do email precisa existir aqui ou na página do produto.

> Regra herdada do projeto: anúncio e email só prometem o que a arte ou a página do
> produto sustentam. Nada de benefício inventado.

## Os dois grupos de arte

A pasta de cada produto separa material com destinos diferentes:

**Na raiz da pasta do produto — assets.** Fotografia de produto e de uso, sem texto
aplicado. São as imagens que entram nas peças.

**Em `<produto>/referencia/` — referências de conteúdo.** Infográficos com título,
ícones e texto sobre a foto. **Não entram nas peças.** Deles sai a informação técnica
que alimenta a copy, e eles mostram como a marca já comunicou cada feature. O tratamento
visual das features em cada peça é criado pelo design a partir dessa informação, nunca
por colagem da arte pronta.

Se você subir um infográfico na raiz por engano, ele acaba tratado como asset. Na dúvida:
tem texto aplicado sobre a imagem, vai para `referencia/`.

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
