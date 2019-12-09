manipulador = open('dadosS1-eth1.txt', 'r')
l = []
i = 0
lista_media = []
lista_diferenca = []
lista_diferenca2 = []
lista_diferenca_final = []
lista_intermediaria = []
lista_final = []
lista_final2 = []
lista_final3 = []
lista_final4 = []
lista_final5 = []
lista_final6 = []
lista_soma = []

for linha in manipulador:
    linha = int(linha.rstrip())
    l.append(linha)

manipulador.seek(0)

#DECOMPOSIÇÃO GRAU 1

print("Sinal original: " + str(l))

for i in range(0, len(l) - 1):

    media = (l[i] + l[i+1]) / 2
    diferenca1 = (l[i] - l[i+1]) / 2
    diferenca2 = (l[i+1] - l[i]) / 2

    #Soma as posições i e i+1
    lista_media.append(media)
    #Diferença das posições i e i+1
    lista_diferenca.append(diferenca1)
    #Diferença das posições i+1 e i
    lista_diferenca2.append(diferenca2)

#Pega as posições necessárias para o cálculo das wavelets
#ex: 1 e 2; 3 e 4; 5 e 6; ...
lista_impar = lista_media[::2]
lista_impar_diferenca1 = lista_diferenca[::2]
lista_impar_diferenca2 = lista_diferenca2[::2]


for a, b in zip(lista_impar_diferenca1, lista_impar_diferenca2):
    f = open('arqListaDif.txt', 'a+')
    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.close()
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(b)


for x in lista_impar:
    lista_intermediaria.append(x)
    lista_final.append(x)
    lista_final.append(x)
    f = open('arqListaMedia.txt', 'a+')
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.close()

print("a1 = " + str(lista_final))

for a, b in zip(lista_final, lista_diferenca_final):
    f = open('arqSoma.txt', 'a+')
    f.write(str(a + b) + "\n")
    f.close()
    lista_soma.append(a + b)

print("d1 = " + str(lista_diferenca_final))

#DECOMPOSIÇÃO GRAU 2

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()

for i in range(0, len(lista_intermediaria) - 1):

    media = (lista_intermediaria[i] + lista_intermediaria[i+1]) / 2
    diferenca1 = (lista_intermediaria[i] - lista_intermediaria[i+1]) / 2
    diferenca2 = (lista_intermediaria[i+1] - lista_intermediaria[i]) / 2

    #Soma as posições i e i+1
    lista_media.append(media)
    #Diferença das posições i e i+1
    lista_diferenca.append(diferenca1)
    #Diferença das posições i+1 e i
    lista_diferenca2.append(diferenca2)


#limpando lista impar 2
lista_intermediaria.clear()

#limpando lista impar diferenca
lista_impar_diferenca1.clear()
lista_impar_diferenca2.clear()

lista_impar2 = lista_media[::2]
lista_impar_diferenca1 = lista_diferenca[::2]
lista_impar_diferenca2 = lista_diferenca2[::2]

#print(lista_impar2)
for x in lista_impar2:
    lista_intermediaria.append(x)
    lista_final2.append(x)
    lista_final2.append(x)
    lista_final2.append(x)
    lista_final2.append(x)
    f = open('arqListaMedia2.txt', 'a+')
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.close()

print("a2 = " + str(lista_final2))

for a, b in zip(lista_impar_diferenca1, lista_impar_diferenca2):
    f = open('arqListaDif2.txt', 'a+')
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.close()
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)

print("d2 = " + str(lista_diferenca_final))


#DECOMPOSIÇÃO GRAU 3

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()


for i in range(0, len(lista_intermediaria) - 1):

    media = (lista_intermediaria[i] + lista_intermediaria[i+1]) / 2
    diferenca1 = (lista_intermediaria[i] - lista_intermediaria[i+1]) / 2
    diferenca2 = (lista_intermediaria[i+1] - lista_intermediaria[i]) / 2

    #Soma as posições i e i+1
    lista_media.append(media)
    #Diferença das posições i e i+1
    lista_diferenca.append(diferenca1)
    #Diferença das posições i+1 e i
    lista_diferenca2.append(diferenca2)


#limpando lista impar 2
lista_intermediaria.clear()

#limpando lista impar diferenca
lista_impar_diferenca1.clear()
lista_impar_diferenca2.clear()

lista_impar3 = lista_media[::2]
lista_impar_diferenca1 = lista_diferenca[::2]
lista_impar_diferenca2 = lista_diferenca2[::2]

#print(lista_impar3)
for x in lista_impar3:
    lista_intermediaria.append(x)
    lista_final3.append(x)
    lista_final3.append(x)
    lista_final3.append(x)
    lista_final3.append(x)
    lista_final3.append(x)
    lista_final3.append(x)
    lista_final3.append(x)
    lista_final3.append(x)
    f = open('arqListaMedia3.txt', 'a+')
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.close()

print("a3 = " + str(lista_final3))

for a, b in zip(lista_impar_diferenca1, lista_impar_diferenca2):
    f = open('arqListaDif3.txt', 'a+')
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.close()
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)

print("d3 = " + str(lista_diferenca_final))


#DECOMPOSIÇÃO GRAU 4

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()


for i in range(0, len(lista_intermediaria) - 1):

    media = (lista_intermediaria[i] + lista_intermediaria[i+1]) / 2
    diferenca1 = (lista_intermediaria[i] - lista_intermediaria[i+1]) / 2
    diferenca2 = (lista_intermediaria[i+1] - lista_intermediaria[i]) / 2

    #Soma as posições i e i+1
    lista_media.append(media)
    #Diferença das posições i e i+1
    lista_diferenca.append(diferenca1)
    #Diferença das posições i+1 e i
    lista_diferenca2.append(diferenca2)


#limpando lista impar 4
lista_impar_diferenca1.clear()
lista_impar_diferenca2.clear()

lista_impar4 = lista_media[::2]
lista_impar_diferenca1 = lista_diferenca[::2]
lista_impar_diferenca2 = lista_diferenca2[::2]

lista_intermediaria.clear()

for x in lista_impar4:
    lista_intermediaria.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    lista_final4.append(x)
    f = open('arqListaMedia4.txt', 'a+')
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.close()

print("a4 = " + str(lista_final4))


for a, b in zip(lista_impar_diferenca1, lista_impar_diferenca2):
    f = open('arqListaDif4.txt', 'a+')
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.close()
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)

print("d4 = " + str(lista_diferenca_final))


#DECOMPOSIÇÃO GRAU 5

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()


for i in range(0, len(lista_intermediaria) - 1):

    media = (lista_intermediaria[i] + lista_intermediaria[i+1]) / 2
    diferenca1 = (lista_intermediaria[i] - lista_intermediaria[i+1]) / 2
    diferenca2 = (lista_intermediaria[i+1] - lista_intermediaria[i]) / 2

    #Soma as posições i e i+1
    lista_media.append(media)
    #Diferença das posições i e i+1
    lista_diferenca.append(diferenca1)
    #Diferença das posições i+1 e i
    lista_diferenca2.append(diferenca2)


#limpando lista impar 5
lista_intermediaria.clear()
#lista_impar5.clear()
lista_impar_diferenca1.clear()
lista_impar_diferenca2.clear()

lista_impar5 = lista_media[::2]
lista_impar_diferenca1 = lista_diferenca[::2]
lista_impar_diferenca2 = lista_diferenca2[::2]


for x in lista_impar5:
    lista_intermediaria.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    lista_final5.append(x)
    f = open('arqListaMedia5.txt', 'a+')
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.close()

print("a5 = " + str(lista_final5))


for a, b in zip(lista_impar_diferenca1, lista_impar_diferenca2):
    f = open('arqListaDif5.txt', 'a+')
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.close()
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)

print("d5 = " + str(lista_diferenca_final))

#DECOMPOSIÇÃO GRAU 6

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()


for i in range(0, len(lista_intermediaria) - 1):

    media = (lista_intermediaria[i] + lista_intermediaria[i+1]) / 2
    diferenca1 = (lista_intermediaria[i] - lista_intermediaria[i+1]) / 2
    diferenca2 = (lista_intermediaria[i+1] - lista_intermediaria[i]) / 2

    #Soma as posições i e i+1
    lista_media.append(media)
    #Diferença das posições i e i+1
    lista_diferenca.append(diferenca1)
    #Diferença das posições i+1 e i
    lista_diferenca2.append(diferenca2)


#limpando lista impar 6
lista_intermediaria.clear()

#lista_impar6.clear()
lista_impar_diferenca1.clear()
lista_impar_diferenca2.clear()

lista_impar6 = lista_media[::2]
lista_impar_diferenca1 = lista_diferenca[::2]
lista_impar_diferenca2 = lista_diferenca2[::2]


for x in lista_impar6:
    lista_intermediaria.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    lista_final6.append(x)
    f = open('arqListaMedia6.txt', 'a+')
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.close()

print("a6 = " + str(lista_final6))


for a, b in zip(lista_impar_diferenca1, lista_impar_diferenca2):
    f = open('arqListaDif6.txt', 'a+')
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.write(str(b) + "\n")
    f.close()
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)
    lista_diferenca_final.append(b)

print("d6 = " + str(lista_diferenca_final))