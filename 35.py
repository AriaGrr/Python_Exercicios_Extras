#Faça um programa que preencha: Uma lista com 3 nomes de lojas. Uma outra lista com 5 nomes de produtos. Uma matriz com os preços de todos os produtos em cada loja. O programa deverá mostrar todas as listas: lojas, produtos e preços (Utilize %3d para imprimir a matriz). Depois, deverá mostrar todas relações (nome do produto – nome da loja - preço) em que o preço não ultrapasse R$ 50,00.

lojas = []
produtos = []
precos = [[0 for i in range(3)] for j in range(5)]

def preencheLojas(lojas):
    for i in range(3):
        lojas.append(input("Digite o nome da loja: "))

def preencheProdutos(produtos):
    for i in range(5):
        produtos.append(input("Digite o nome do produto: "))

def preenchePrecos(precos):
    for j in range(3):
        for i in range(5):
            precos[i][j] = int(input("Digite o preco do produto %s na loja %s: " % (i, j)))

def imprimeLojas(lojas):
    print()
    print("Lojas: ")
    for i in range(3):
        print(lojas[i])

def imprimeProdutos(produtos):
    print()
    print("Produtos: ")
    for i in range(5):
        print(produtos[i])

def imprimePrecos(precos):
    for j in range(3):
        if j > 0:
            print()
        for i in range(5):
            print("%3d" % precos[i][j], end = " ")

def imprimeRelacoes(lojas, produtos, precos):
    for j in range(3):
        if j > 0:
            print()
        for i in range(5):
            if precos[i][j] < 50:
                print("Loja: %s, produto %s e preço %d" % (lojas[j], produtos[i], precos[i][j]))

def main():
    preencheLojas(lojas)
    preencheProdutos(produtos)
    preenchePrecos(precos)
    imprimeLojas(lojas)
    imprimeProdutos(produtos)
    print()
    print("Preços: ")
    imprimePrecos(precos)
    print()
    print()
    print("Preços menores que R$ 50.00: ")
    imprimeRelacoes(lojas, produtos, precos)

main()