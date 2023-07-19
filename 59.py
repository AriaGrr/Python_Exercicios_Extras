#Crie uma matriz m[12][12] com números inteiros aleatórios (de 0 até 99, randint(0,99)) . Em seguida, calcule e mostre a soma considerando somente aqueles elementos que estão na área inferior da matriz, conforme ilustrado abaixo (área verde).

from random import randint

matriz = [[randint(0,99) for i in range(12)] for j in range(12)]
soma = 0

soma += sum(matriz[7][5:6])
soma += sum(matriz[8][4:7])
soma += sum(matriz[9][3:8])
soma += sum(matriz[10][2:9])
soma += sum(matriz[11][1:10])

print("Matriz original: ")
for i in range(12):
    for j in range(12):
        print("%3d" % matriz[i][j], end=" ")
    print()

print()
print("Soma: %d" %soma)

