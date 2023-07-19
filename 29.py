#Faça um Programa que leia 20 números inteiros e armazene-os em uma lista. Armazene os números pares na lista par e os números ímpares na lista impar. Imprima as três listas no final.

lista = []
par = []
impar = []
for i in range(20):
    a = int(input(""))
    lista.append(a)
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)

for i in range(len(lista)):
    print(lista[i], end = " ")
print("")

for i in range(len(impar)):
    print(impar[i], end = " ")
print("")
    
for i in range(len(par)):
    print(par[i], end = " ")
print("")




