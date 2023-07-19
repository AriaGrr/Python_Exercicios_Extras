# Faça o ciclo do zodiaco chines com o operador %

a = int(input("Digite um ano: "))

if a % 12 == 0:
    print(f"{a} é o ano do(a) Macaco")
elif a % 12 == 1:
    print(f"{a} é o ano do(a) Galo")
elif a % 12 == 2:
    print(f"{a} é o ano do(a) Cachorro")
elif a % 12 == 3:
    print(f"{a} é o ano do(a) Porco")
elif a % 12 == 4:
    print(f"{a} é o ano do(a) Rato")
elif a % 12 == 5:
    print(f"{a} é o ano do(a) Boi")
elif a % 12 == 6:
    print(f"{a} é o ano do(a) Tigre")
elif a % 12 == 7:
    print(f"{a} é o ano do(a) Coelho")
elif a % 12 == 8:
    print(f"{a} é o ano do(a) Dragão")
elif a % 12 == 9:
    print(f"{a} é o ano do(a) Serpente")
elif a % 12 == 10:
    print(f"{a} é o ano do(a) Cavalo")
elif a % 12 == 11:
    print(f"{a} é o ano do(a) Carneiro")
else:
    print("Erro!")