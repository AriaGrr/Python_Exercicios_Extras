# Sabendo que a distância entre dois pontos p0 e p1 pode ser calculada usando: distancia = sqrt((p0_x - p1_x)**2 + (p0_y - p1_y)**2), faça um programa que recebe os valores dos pontos e imprime a distância entre eles. O programa deve parar de receber valores quando o usuário entrar com a palavra "sair".

from math import sqrt

while True:
    p0_x = input("valor de X para P0: ")
    if p0_x == "sair":
        break
    p0_y = input("valor de Y para P0: ")
    if p0_y == "sair":
        break
    p1_x = input("valor de X para P1: ")
    if p1_x == "sair":
        break
    p1_y = input("valor de Y para P1: ")
    if p1_y == "sair":
        break
    distancia = sqrt((float(p0_x) - float(p1_x))**2 + (float(p0_y) - float(p1_y))**2)
    print(f"Distância de {distancia}")
