#Faça um programa que calcule a média e o desvio padrão de um vetor com os valores e o número de elementos definido pelo usuário.

a = int(input("Qual o tamanho da lista: "))
b = 0
c = []
d = 0
e = 0
f = 0

print(f"Digite os valores:")
while b < a:
    c.append(int(input(f"")))
    b += 1

for i in range(a):
    d += c[i]
d = d/a

for i in range(a):
    e += (c[i] - d)**2
e = e/a
e = e**(1/2)

print(f"Média = {d :.2f} e Desvio = {e :.4f}")

