#Faça um programa que leia a dimensão dos vetores a serem multiplicados, em seguida os componentes de cada vetor, e apresente como resultado o resultado escalar.

a = []
b = []
c = 0

print ("Digite o vetor 1: ")
for i in range(3):
    a.append(int(input("")))
print ("Digite o vetor 2: ")
for i in range(3):
    b.append(int(input("")))

for i in range(3):
    c += a[i] * b[i]

print (c)