# Faça um programa que preencha uma matriz M (2x2), solicitando cada elemento (números inteiros) para o usuário. Depois, calcule e mostre uma matriz resultante da multiplicação dos elementos de M pelo seu maior elemento. Utilize %3d para imprimir a matriz.

# Função que preenche a matriz
def preencheMatriz(matriz):
    for i in range(2):
        for j in range(2):
            matriz[i][j] = int(input("Digite o elemento da linha %d e coluna %d: " % (i,j)))

# Função que calcula o maior elemento da matriz
def maiorElemento(matriz):
    maior = 0
    for i in range(2):
        for j in range(2):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    return maior

# Função que calcula a matriz resultante
def calculaMatriz(matriz, maior):
    for i in range(2):
        for j in range(2):
            matriz[i][j] = matriz[i][j] * maior

# Função que imprime a matriz
def imprimeMatriz(matriz):
    for i in range(2):
        for j in range(2):
            print(" %d" % matriz[i][j], end=" ")
        print()

# Função principal
def main():
    matriz = [[0 for i in range(2)] for j in range(2)]
    preencheMatriz(matriz)
    maior = maiorElemento(matriz)
    calculaMatriz(matriz, maior)
    print("Matriz resultante: ")
    imprimeMatriz(matriz)

# Chamada da função principal
main()