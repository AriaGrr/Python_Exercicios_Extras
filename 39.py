#Crie um programa que preencha uma matriz 20x10 (20 linhas e 10 colunas) com números inteiros aleatórios (entre 0 e 10) e some cada uma das linhas, armazenando o resultado das somas em um vetor (lista). A seguir, o programa deverá multiplicar cada elemento da matriz pela soma da linha correspondente e mostrar a matriz resultante.

from random import randint

matriz = [[randint(0, 10) for i in range(10)] for j in range(20)]
vetor = [0 for j in range(20)]
multiplica = [[0 for i in range(10)] for j in range(20)]

def somaLinhas(matriz,vetor):
    for j in range(20):
        for i in range(10):
            if i == 0:
                vetor[j] = sum(matriz[j])
            else:
                vetor[j] = sum(matriz[j]) + vetor[j - 1]

def multiplicaMatriz(matriz,vetor,multiplica):
    for j in range(20):
        for i in range(10):
            multiplica[j][i] = matriz[j][i] * vetor[j]

def imprime(matriz,vetor,multiplica):
    print("Matriz original: ")
    for j in range(20):
        if j > 0:
            print()
        for i in range(10):
            print("%3d" % matriz[j][i], end = " ")
    print()
    print()
    print ("Vetor com a somatória de cada linha:")
    print (vetor)
    print()
    print ("matriz depois da multiplicação:")
    for j in range(20):
        if j > 0:
            print()
        for i in range(10):
            print ("%5d" % multiplica[j][i], end = " ")

def main():
    somaLinhas(matriz,vetor)
    multiplicaMatriz(matriz,vetor,multiplica)
    imprime(matriz,vetor,multiplica)

main()

