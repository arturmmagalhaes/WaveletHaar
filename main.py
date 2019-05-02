manipulador = open('canal1.txt', 'r')
l = []
i = 0
lista_media = []
lista_diferenca = []
lista_diferenca2 = []
lista_diferenca_final = []
lista_final = []
lista_soma = []

for linha in manipulador:
    linha = int(linha.rstrip())
    l.append(linha)

manipulador.seek(0)

#DECOMPOSIÇÃO NÍVEL 1
#OK
#MÉDIA1 = a1

#OK
#DIFERENÇA = d1

#OK
#SOMA s1 = a1 + d1

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
    lista_final.append(x)
    lista_final.append(x)
    f = open('arqListaMedia.txt', 'a+')
    f.write(str(x) + "\n")
    f.write(str(x) + "\n")
    f.close()

print("a1 = " + str(lista_final))
print("d1 = " + str(lista_diferenca_final))


for a, b in zip(lista_final, lista_diferenca_final):
    f = open('arqSoma.txt', 'a+')
    f.write(str(a + b) + "\n")
    f.close()
    lista_soma.append(a + b)

print("s1 = a1 + d1 => " + str(lista_soma))