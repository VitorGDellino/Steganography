# Esteganografia
Projeto final de Processamento de Imagens.

## Contribuidores

Giuliano Lourençon  10295590<br />
Vitor Giovani Dellinocente 9277875<br />

## Tema
O Projeto se chama Hiding Message Maker (HMM).<br />
O tema escolhido para o projeto foi a esteganografia, que visa esconder dados dentro de uma imagem, esse dados podem ser textos, programas e até mesmo outras imagens. 

## Exemplos de Imagens
![Imagem Montanha](https://github.com/VitorGDellino/Steganography/blob/master/images/mountain.jpg)<br />
[Fonte](https://wallpapersite.com/nature/reine-lake-mountains-norway-4k-4899.html)<br />

![Imagem Mar](https://github.com/VitorGDellino/Steganography/blob/master/images/sea.jpg)<br />
[Fonte](https://br.pinterest.com/pin/24629129192697872)<br />

![Imagem Tigre](https://github.com/VitorGDellino/Steganography/blob/master/images/tiger.jpg)<br />
[Fonte](http://www.img.pink/image/fv)<br />

![Imagem Cachoeira](https://github.com/VitorGDellino/Steganography/blob/master/images/waterfall.jpg)<br />
[Fonte](https://wallpapersite.com/nature/tropical-forest-waterfall-hd-4k-6161.html)<br />

## Métodos
Em princípio iremos implementar o LSB (Least Significant Bits). No nosso caso como esconderemos textos, a técnica utilizada será, utilizar 3 pixeis para esconder uma unica letra (8 bits), pois em cada pixel, existem três canais de cores, vermelho, verde e azul (rgb), assim podemos utilizar 3 bits a cada 1 pixel para esconder uma parte da letra, totalizando 3 pixeis para armazenar a letra completa. Após feito o LSB, pretendemos implementar outro algoritmo, baseado no LSB, porém com o diferencial de que um caracter é armazenado em 8 pixeis sendo cada bit em um pixel e este será formado com a equação lógica de XOR entre os bits menos significativos de cada canal de cor do pixel, para que ao fim possamos compará-los. 
