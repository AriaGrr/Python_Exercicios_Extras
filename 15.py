# Escreva um programa que exiba uma tabela de conversão de temperatura de graus Celsius para graus Fahrenheit. A tabela deve incluir linhas para todas as temperaturas (de 5 em 5 graus Celsius ) entre um valor inteiro mínimo e um valor inteiro máximo (incluso) digitados pelo usuário. Inclua cabeçalhos apropriados em suas colunas.

a = int(input("Digite o valor mínimo em graus C: "))
b = int(input("Digite o valor máximo em graus C: "))

print("  Temperatura em C   Temperatura em F")

while a <= b:
    c = a*1.8+32
    #print(f"{a} {c :.0f}")
    print("%18d %18.0f" % (a, c))
    a += 5





