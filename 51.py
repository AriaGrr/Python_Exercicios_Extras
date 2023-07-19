#Escreva uma função chamada acha_palavra, que recebe uma palavra como parâmetro e conta e exibe a quantidade de ocorrências dessa palavra em um arquivo chamado "busca.txt". Entregue apenas a função.

def acha_palavra(palavra):
    if palavra in ['e', 'a', 'o']:
        with open("busca.txt") as f:
            conteudo = f.read()
            palavras = conteudo.split()
            contagem = sum(p.lower() in ['e', 'a', 'o'] for p in palavras)
            print(f"{contagem}")
    else:
        with open("busca.txt") as f:
            conteudo = f.read()
            palavras = conteudo.split()
            contagem = conteudo.lower().count(palavra.lower())
            print(f"{contagem}")

            