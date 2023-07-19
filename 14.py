#Faça um programa que leia uma quantidade de números que será digitada pelo usuário. Em seguida, digite todos os números, conforme quantidade previamente informada, e exiba o maior deles.

a = int(input("Entre com a quantidade de números que serão digitados: "))

b = 0
c = -10000

while b < a:
    d = int(input(f"número {b+1}: "))
    if d > c:
        c = d
    b += 1

print(f"Maior número digitado: {c}")

