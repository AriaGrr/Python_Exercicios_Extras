# Elabore um programa que preencha uma matriz 4x2 com números inteiros recebidos do usuário e mostre essa matriz. Calcule e mostre quantos elementos dessa matriz são maiores que 10 e, em seguida, mostre uma segunda matriz com 0 (zero) no lugar dos elementos maiores que 10. Utilize %3d para imprimir todas as matrizes.

matriz = [[0 for i in range(2)] for j in range(4)]
matriz2 = [[0 for i in range(2)] for j in range(4)]
maior = []

def preencheMatriz(matriz):
    for j in range(4):
        for i in range(2):
            matriz[j][i] = int(input(f"Digite o elemento da linha {j} e coluna {i}: "))
            if matriz[j][i] < 10:
                matriz2[j][i] = matriz[j][i]
            else:
                maior.append(matriz[j][i])

def imprime(matriz):
    print("Matriz original: ")
    for j in range(4):
        if j > 0:
            print()
        for i in range(2):
            print("%3d" % matriz[j][i], end = " ")
    print()
    print()
    for i in range(len(maior)):
        print(f"{maior[i]} é maior que 10!")
    print("No total, %d elementos são maiores que 10!" % len(maior))
    print()
    print("Matriz sem os números maiores que 10: ")
    for j in range(4):
        if j > 0:
            print()
        for i in range(2):
            print("%3d" % matriz2[j][i], end = " ")

def main():
    preencheMatriz(matriz)
    imprime(matriz)

main()