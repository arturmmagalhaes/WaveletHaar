import matplotlib.pyplot as plt

def waveletHaar(lista):
    for i in range(0, len(lista) - 1):
        media = (lista[i] + lista[i + 1]) / 2
        diferenca1 = (lista[i] - lista[i + 1]) / 2
        diferenca2 = (lista[i + 1] - lista[i]) / 2

        # Soma as posições i e i+1
        lista_media.append(media)
        # Diferença das posições i e i+1
        lista_diferenca.append(diferenca1)
        # Diferença das posições i+1 e i
        lista_diferenca2.append(diferenca2)

def armazenar_lista_dif(n, lista_diferenca, lista_diferenca2):
    for a, b in zip(lista_diferenca[::2], lista_diferenca2[::2]):
        if n == 1:
            f = open('ListaDifereca1.txt', 'a+')
            f.write(str(a) + "\n")
            f.write(str(b) + "\n")
            f.close()
            lista_diferenca_final.append(a)
            lista_diferenca_final.append(b)
        elif n == 2:
            i = 1
            j = 1
            while i <= 2:
                f = open('ListaDifereca2.txt', 'a+')
                f.write(str(a) + "\n")
                lista_diferenca_final.append(a)
                i += 1
            while j <= 2:
                f.write(str(b) + "\n")
                lista_diferenca_final.append(b)
                j += 1
            f.close()
        elif n == 3:
            i = 1
            j = 1
            while i <= 4:
                f = open('ListaDifereca3.txt', 'a+')
                f.write(str(a) + "\n")
                lista_diferenca_final.append(a)
                i += 1
            while j <= 4:
                f.write(str(b) + "\n")
                lista_diferenca_final.append(b)
                j += 1
            f.close()
        elif n == 4:
            i = 1
            j = 1
            while i <= 8:
                f = open('ListaDifereca4.txt', 'a+')
                f.write(str(a) + "\n")
                lista_diferenca_final.append(a)
                i += 1
            while j <= 8:
                f.write(str(b) + "\n")
                lista_diferenca_final.append(b)
                j += 1
            f.close()
        elif n == 5:
            i = 1
            j = 1
            while i <= 16:
                f = open('ListaDifereca5.txt', 'a+')
                f.write(str(a) + "\n")
                lista_diferenca_final.append(a)
                i += 1
            while j <= 16:
                f.write(str(b) + "\n")
                lista_diferenca_final.append(b)
                j += 1
            f.close()
        elif n == 6:
            i = 1
            j = 1
            while i <= 32:
                f = open('ListaDifereca6.txt', 'a+')
                f.write(str(a) + "\n")
                lista_diferenca_final.append(a)
                i += 1
            while j <= 32:
                f.write(str(b) + "\n")
                lista_diferenca_final.append(b)
                j += 1
            f.close()

def armazenar_lista_med(n, lista_media):
    for x in lista_media[::2]:
        lista_intermediaria.append(x)
        i = 1
        if n == 1:
            f = open('ListaMedia1.txt', 'a+')
            while i <= 2:
                lista_final.append(x)
                f.write(str(x) + "\n")
                i += 1
            f.close()
        elif n == 2:
            f = open('ListaMedia2.txt', 'a+')
            while i <= 4:
                lista_final2.append(x)
                f.write(str(x) + "\n")
                i += 1
            f.close()
        elif n == 3:
            f = open('ListaMedia3.txt', 'a+')
            while i <= 8:
                lista_final3.append(x)
                f.write(str(x) + "\n")
                i += 1
            f.close()
        elif n == 4:
            f = open('ListaMedia4.txt', 'a+')
            while i <= 16:
                lista_final4.append(x)
                f.write(str(x) + "\n")
                i += 1
            f.close()
        elif n == 5:
            f = open('ListaMedia5.txt', 'a+')
            while i <= 32:
                lista_final5.append(x)
                f.write(str(x) + "\n")
                i += 1
            f.close()
        elif n == 6:
            f = open('ListaMedia6.txt', 'a+')
            while i <= 64:
                lista_final6.append(x)
                f.write(str(x) + "\n")
                i += 1
            f.close()

manipulador = open('dados.txt', 'r')
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

waveletHaar(l)

armazenar_lista_med(1, lista_media)

armazenar_lista_dif(1, lista_diferenca, lista_diferenca2)

print("a1 = " + str(lista_final))

print("d1 = " + str(lista_diferenca_final))


#DECOMPOSIÇÃO GRAU 2

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()

waveletHaar(lista_intermediaria)

#limpando lista_intermediaria
lista_intermediaria.clear()

armazenar_lista_med(2, lista_media)

armazenar_lista_dif(2, lista_diferenca, lista_diferenca2)

print("a2 = " + str(lista_final2))

print("d2 = " + str(lista_diferenca_final))


#DECOMPOSIÇÃO GRAU 3

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()

waveletHaar(lista_intermediaria)

#limpando lista_intermediaria
lista_intermediaria.clear()

armazenar_lista_med(3, lista_media)

armazenar_lista_dif(3, lista_diferenca, lista_diferenca2)

print("a3 = " + str(lista_final3))

print("d3 = " + str(lista_diferenca_final))


#DECOMPOSIÇÃO GRAU 4

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()

waveletHaar(lista_intermediaria)

#limpando lista_intermediaria
lista_intermediaria.clear()

armazenar_lista_med(4, lista_media)

armazenar_lista_dif(4, lista_diferenca, lista_diferenca2)

print("a4 = " + str(lista_final4))

print("d4 = " + str(lista_diferenca_final))


#DECOMPOSIÇÃO GRAU 5

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()

waveletHaar(lista_intermediaria)

#limpando lista_intermediaria
lista_intermediaria.clear()

armazenar_lista_med(5, lista_media)

armazenar_lista_dif(5, lista_diferenca, lista_diferenca2)

print("a5 = " + str(lista_final5))


print("d5 = " + str(lista_diferenca_final))


#DECOMPOSIÇÃO GRAU 6

#limpando lista media
lista_media.clear()

#limpando lista diferenca
lista_diferenca.clear()
lista_diferenca2.clear()
lista_diferenca_final.clear()

waveletHaar(lista_intermediaria)

#limpando lista_intermediaria
lista_intermediaria.clear()

armazenar_lista_med(6, lista_media)

armazenar_lista_dif(6, lista_diferenca, lista_diferenca2)

print("a6 = " + str(lista_final6))

print("d6 = " + str(lista_diferenca_final))

plt.subplot(611)
plt.plot(lista_final)
plt.subplot(612)
plt.plot(lista_final2)
plt.subplot(613)
plt.plot(lista_final3)
plt.subplot(614)
plt.plot(lista_final4)
plt.subplot(615)
plt.plot(lista_final5)
plt.subplot(616)
plt.plot(lista_final6)
plt.show()