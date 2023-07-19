#Faça um programa que receba um número inteiro maior que 1 e verifique se o número fornecido é primo ou não. Mostre uma mensagem de número primo ou de número não primo. Um número é primo quando é divisível apenas pelo número um e por ele mesmo.
a = int(input("Digite o número desejado: "))
b = 2
c = 0

while b < a:
    if a % b == 0:
        c += 1
    b += 1

if c == 0:
    print("Número primo")
else:
    print("Número não primo")

    