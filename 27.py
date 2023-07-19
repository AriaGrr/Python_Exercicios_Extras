#Faça um programa que leia uma a um modelos de cinco carros (exemplos: FUSCA, GOL, VECTRA etc) e os guarde em uma mesma lista. Leia (um a um) uma outra lista  com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre: - O modelo do carro mais econômico; - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros.

carros = []
consumo = []
for i in range(5):
    carros.append(input(""))

for i in range(5):
    consumo.append(float(input("")))

print(f"{carros[consumo.index(max(consumo))]}")

for i in range(5):
    print(f"{1000/consumo[i] :.0f}")



