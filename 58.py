#Faça um programa que leia valores em uma lista e o decomponha em outras duas listas, uma contendo os elementos que são múltiplos de 2 ou 3 na lista original e a outra contendo os elementos que não são.Observação: A lista original já está declarada no Moodle, chamada lista (conforme exemplos abaixo); somente use-a no código. Cuidado, pois nos casos de teste a lista nem sempre tem o mesmo tamanho. 

lista = [int(i) for i in input().split()]
lista1 = []
lista2 = []

for i in lista:
    if i % 2 == 0 or i % 3 == 0:
        lista1.append(i)
    else:
        lista2.append(i)

print(lista1)
print(lista2)