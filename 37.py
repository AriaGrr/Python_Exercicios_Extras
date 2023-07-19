#Crie um programa que preencha uma matriz 20x10 (20 linhas e 10 colunas) com números inteiros aleatórios (entre 0 e 10) e some cada uma das linhas, armazenando o resultado das somas em um vetor (lista). A seguir, o programa deverá multiplicar cada elemento da matriz pela soma da linha correspondente e mostrar a matriz resultante.

from random import randint

matriz = [[0 for i in range(10)] for j in range(20)]
vetor = [0 for i in range(20)]
matriz2 = [[0 for i in range(10)] for j in range(20)]

def preencheMatriz(matriz):
    for j in range(20):
        for i in range(10):
            matriz[j][i] = randint(0, 10)

def somaLinhas(matriz, vetor):
    for j in range(20):
        for i in range(10):
            vetor[j] += matriz[j][i]

def multiplicaMatriz(matriz, vetor, matriz2):
    for j in range(20):
        for i in range(10):
            matriz2 = matriz[j][i] * vetor[j]


def imprime(matriz, vetor, matriz2):
    print("Matriz original: ")
    for j in range(20):
        if j > 0:
            print()
        for i in range(10):
            print("%3d" % matriz[j][i], end = " ")
    print()
    print()
    print("Vetor com a somatoria de cada linha: ")
    print(vetor)
    print()
    print("matriz depois da multiplicação: ")
    for j in range(20):
        if j > 0:
            print()
        for i in range(10):
            print("%5d" % matriz2[j][i], end = " ")

def main():
    preencheMatriz(matriz)
    somaLinhas(matriz, vetor)
    multiplicaMatriz(matriz, vetor, matriz2)
    imprime(matriz, vetor, matriz2)

main()