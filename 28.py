#Crie um programa que leia números inteiros do usuário até que o número 0 seja inserido. Uma vez que todos os números inteiros tenham sido lidos, seu programa deve exibir todos os números negativos, seguidos por todos os números positivos. Dentro de cada grupo, os números devem ser exibidos na mesma ordem em que foram inseridos pelo usuário

a = int(input(""))
b = []
c = []
d = 0

while a != 0:
    if a < 0:
        b.append(a)
    else:
        c.append(a)
    a = int(input(""))

append = repr(b + c)

while d < len(append):
    print(append[d], end = "")
    d += 1
