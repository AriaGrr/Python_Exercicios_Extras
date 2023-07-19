#Implemente uma função que receba um nome completo e apresente apenas o último nome e o 1o nome na seguinte forma: último, 1o nome.

def nomeCitacao(nome):
    nome = nome.split()
    print(f"{nome[-1]}, {nome[0]}")