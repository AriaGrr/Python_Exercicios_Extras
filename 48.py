#Escreva uma função chamada conta_palavras que conte e exibe e quantidade de palavras contidas em um arquivo chamado "palavras.txt". Entregue apenas a função.

def conta_palavras():
    with open("palavras.txt") as f:
        print(f"Quantidade de palavras:  {len(f.read().split())}")

