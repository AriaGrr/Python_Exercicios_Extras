# Escreva uma função que recebe uma lista de números inteiros e retorne uma nova lista que contém o quadrado de cada um desses números. Você só precisa entregar o código da função.

def quadrado(lista):
    lista2 = []
    for i in range(len(lista)):
        lista2.append(lista[i]**2)
    return lista2

