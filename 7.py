b = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
a = float(input("Digite o valor da aresta a em metros: "))

if b == "dodecaedro" :
    v = ((15+7*(5**(1/2)))/4)*(a**3)
elif b == "icosaedro":
    v = (5/12)*(3+(5**(1/2)))*(a**3)

print("O volume de um %s regular com %.2f de aresta é: %.2f" %(b, a, v))