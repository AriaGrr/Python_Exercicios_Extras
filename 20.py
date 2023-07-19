
import math

def main():
    latA = float(input("Digite a latitude A: "))
    longA = float(input("Digite a longitude A: "))
    latB = float(input("Digite a latitude B: "))
    longB = float(input("Digite a longitude B: "))

    distancia = 6371.01 * math.acos(math.sin(math.radians(latA)) * math.sin(math.radians(latB)) + math.cos(math.radians(latA)) * math.cos(math.radians(latB)) * math.cos(math.radians(longA) - math.radians(longB)))

    print(f"A distância é {distancia :.2f}km.")

main()

