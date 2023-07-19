#Crie uma função chamada lista_arquivo, que recebe uma lista de palavras, escreve cada uma dessas palavras em um arquivo e exibe o conteúdo do arquivo. Entregue apenas a função.

def lista_arquivo(lista):
    with open("arquivo.txt", "w") as f:
        for i in lista:
            f.write(i + "\n")
    with open("arquivo.txt") as f:
        print(f.read())



