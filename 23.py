#Crie uma função para calcular e retornar o peso de uma pessoa nos outros planetas do Sistema Solar. A função deve ter dois parâmetros: o planeta desejado e o peso em Kg da pessoa na Terra. O programa principal deve receber o peso da pessoa na Terra (em Kg) e o planeta desejado.Relação de pesos: 1 Kg na Terra equivale a: 0.37 Kg em Mercúrio; 0.88 Kg em Vênus; 0.38 Kg em Marte; 2.64 Kg em Júpiter; 1.15 Kg em Saturno; 1.17 Kg em Urano; e 1.18 Kg em Netuno. 

def peso(terra, planeta):
    if planeta == "Mercúrio":
        return terra*0.37
    elif planeta == "Vênus":
        return terra*0.88
    elif planeta == "Marte":
        return terra*0.38
    elif planeta == "Júpiter":
        return terra*2.64
    elif planeta == "Saturno":
        return terra*1.15
    elif planeta == "Urano":
        return terra*1.17
    elif planeta == "Netuno":
        return terra*1.18
    else:
        return "Planeta não encontrado"

b = input("Digite o nome do planeta desejado: ")
a = float(input("Digite o peso da pessoa na Terra em kg: "))
print(f"Peso em {b}: {peso(a, b) :.2f}")
