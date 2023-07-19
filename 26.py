#Em uma determinada jurisdição, as tarifas de táxi consistem em uma tarifa básica de R$ 10.00, mais R$ 0.50 para cada 125 metros percorridos. Escreva uma função que considere a distância percorrida (em quilômetros inteiros) como seu único parâmetro e retorne a tarifa total como seu único resultado. Escreva um programa principal em que a quantidade de km será digitada e onde a função será chamada.

def taxi(km):
    return 10 + (km*1000/125)*0.5

a = float(input("Digite a quantidade de quilômetros: "))
print(f"Tarifa {taxi(a) :.2f}")