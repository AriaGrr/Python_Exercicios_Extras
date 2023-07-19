from random import randint

matriz = [[randint(0, 10) for i in range(10)] for j in range(20)]
vetor = [0 for i in range(20)]
multiplica = [[0 for i in range(10)] for j in range(20)]

print("Matriz original: ")
for j in range(20):
    if j > 0:
        print()
    for i in range(10):
        print("%3d" % matriz[j][i], end = " ")
print()

vetor [0] = matriz[0][0]
for j in range(20):
    for i in range(10):
        vetor[j] += matriz[j][i]

print()
print("Vetor com a somatoria de cada linha: ")
print(vetor)
print()