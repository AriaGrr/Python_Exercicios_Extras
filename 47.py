#Escreva uma função chamada read_file que abre e exibe o conteúdo de um arquivo chamado "poema.txt". Escreva apenas a função.

def read_file():
    with open("poema.txt") as f:
        print(f.read())