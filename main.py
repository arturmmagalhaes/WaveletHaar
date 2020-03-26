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

#Pega as posições necessárias para o cálculo das wavelets -> [::2}
#ex: 1 e 2; 3 e 4; 5 e 6; ...


for a, b in zip(lista_diferenca[::2], lista_diferenca2[::2]):
    f = open('arqListaDif.txt', 'a+')
    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.close()
    lista_diferenca_final.append(a)
    lista_diferenca_final.append(b)


for x in lista_media[::2]:
    lista_intermediaria.append(x)
    f = open('arqListaMedia.txt', 'a+')
    i = 1
    while i<=2:
        lista_final.append(x)
        f.write(str(x) + "\n")
        i+=1
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

#limpando lista_intermediaria
lista_intermediaria.clear()

for x in lista_media[::2]:
    lista_intermediaria.append(x)
    f = open('arqListaMedia2.txt', 'a+')
    i = 1
    while i <= 4:
        lista_final2.append(x)
        f.write(str(x) + "\n")
        i+=1
    f.close()

print("a2 = " + str(lista_final2))

for a, b in zip(lista_diferenca[::2], lista_diferenca2[::2]):
    f = open('arqListaDif2.txt', 'a+')
    i = 1
    j = 1
    while i <= 2:
        f.write(str(a) + "\n")
        lista_diferenca_final.append(a)
        i+=1
    while j <= 2:
        f.write(str(b) + "\n")
        lista_diferenca_final.append(b)
        j+=1
    f.close()

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


#limpando lista_intermediaria
lista_intermediaria.clear()


for x in lista_media[::2]:
    lista_intermediaria.append(x)
    f = open('arqListaMedia3.txt', 'a+')
    i=1
    while i<=8:
        lista_final3.append(x)
        f.write(str(x) + "\n")
        i+=1
    f.close()

print("a3 = " + str(lista_final3))

for a, b in zip(lista_diferenca[::2], lista_diferenca2[::2]):
    f = open('arqListaDif3.txt', 'a+')
    i = 1
    j = 1
    while i <= 4:
        f.write(str(a) + "\n")
        lista_diferenca_final.append(a)
        i+=1
    while j <= 4:
        f.write(str(b) + "\n")
        lista_diferenca_final.append(b)
        j+=1
    f.close()

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

lista_intermediaria.clear()

for x in lista_media[::2]:
    lista_intermediaria.append(x)
    f = open('arqListaMedia4.txt', 'a+')
    i=1
    while i <= 16:
        lista_final4.append(x)
        f.write(str(x) + "\n")
        i+=1
    f.close()

print("a4 = " + str(lista_final4))

for a, b in zip(lista_diferenca[::2], lista_diferenca2[::2]):
    f = open('arqListaDif4.txt', 'a+')
    i=1
    j=1
    while i <= 8:
        f.write(str(a) + "\n")
        lista_diferenca_final.append(a)
        i+=1
    while j <= 8:
        f.write(str(b) + "\n")
        lista_diferenca_final.append(b)
        j+=1
    f.close()

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

#limpando lista_intermediaria
lista_intermediaria.clear()

for x in lista_media[::2]:
    lista_intermediaria.append(x)
    f = open('arqListaMedia5.txt', 'a+')
    i=1
    while i <= 32:
        lista_final5.append(x)
        f.write(str(x) + "\n")
        i+=1
    f.close()

print("a5 = " + str(lista_final5))

for a, b in zip(lista_diferenca[::2], lista_diferenca2[::2]):
    f = open('arqListaDif5.txt', 'a+')
    i = 1
    j = 1
    while i <= 16:
        f.write(str(a) + "\n")
        lista_diferenca_final.append(a)
        i += 1
    while j <= 16:
        f.write(str(b) + "\n")
        lista_diferenca_final.append(b)
        j += 1
    f.close()

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

#limpando lista_intermediaria
lista_intermediaria.clear()

for x in lista_media[::2]:
    lista_intermediaria.append(x)
    f = open('arqListaMedia6.txt', 'a+')
    i = 1
    while i <= 64:
        lista_final6.append(x)
        f.write(str(x) + "\n")
        i += 1
    f.close()

print("a6 = " + str(lista_final6))

for a, b in zip(lista_diferenca[::2], lista_diferenca2[::2]):
    f = open('arqListaDif6.txt', 'a+')
    i = 1
    j = 1
    while i <= 32:
        f.write(str(a) + "\n")
        lista_diferenca_final.append(a)
        i += 1
    while j <= 32:
        f.write(str(b) + "\n")
        lista_diferenca_final.append(b)
        j += 1
    f.close()

print("d6 = " + str(lista_diferenca_final))