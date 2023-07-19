#Escreva uma função chamada line_count que conte e exiba a quantidade de linhas que não começam com a letra "E" em um arquivo chamado "story.txt". Entregue apenas a função.

def line_count():
    with open("story.txt") as f:
        linhas = f.readlines()
        contagem = sum(l[0] != "E" for l in linhas)
        print(f"Numero de linhas que nao comecam com 'E'= {contagem}")


