# WaveletHaar

A palavra Wavelet se origina de "Ondelette"e significa onda pequena, como apresentada por Gutierrez (2002). As wavelets estão sendo estudadas por diversos matemáticos nos últimos anos, pois, elas podem ser aplicadas em várias áreas como: redes de computadores,
processamento de sinais, processamento de imagem, equações diferenciais, entre outras. As primeiras wavelets apresentadas foram as Wavelets de Haar em 1909, porém ficaram esquecidas por bastante tempo. Em 1985, Mallat estimulou outros pesquisadores a utilizarem-nas por causa do seu trabalho em processamento digital de imagens. Mallat (1989) desenvolveu uma teoria denominada análise de multirresolução. Em 1990, Daubechies construiu um conjunto de bases ortonormais de wavelets baseado nos trabalhos de Mallat.

# Esquema Lifting

O Esquema Lifting, desenvolvido por Sweldens (1997), é facilmente implementado em qualquer linguagem de programação e pode ser utilizado para auxiliar na convolução dos coeficientes de aproximação e dos detalhes de um sinal. Sejam a e b dois números consecutivos de uma amostra de tamanho 2^n, pode-se fazer uma transformação linear, tal que, substituiremos a e b pela sua média s e por sua diferença d: 

s = (a + b) / 2      

d = b − a.

_______________________________________________________________________________________________________________________________________

# Referências

GUTIERREZ, C. E. C. Eliminação do ruído por encolhimento de Wavelets: Uma aplicação
à série de preço Spot de energia elétrica do brasil. Dissertação (Mestrado em Engenharia
Elétrica) — Programa de Pós-Graduação em Sistemas de Energia Elétrica do Departamento de
Engenharia Elétrica, Pontifícia Universidade Católica do Rio de Janeiro, Rio de Janeiro, 2002.

MALLAT, S. G. A theory for multiresolution signal decomposition: The wavelet representation.
IEEE Transactions on Pattern Analysis Machine Intelligence, v. 11, p. 674–693, 1989.

SWELDENS, W. The lifting scheme: A construction of second generation wavelets. SIAM
Journal on Mathematical Analysis, Murray Hill, New Jersey, v. 29, n. 2, p. 511–546, 1997.
