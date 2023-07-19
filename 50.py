#Escreva uma função chamada acha_palavra, que recebe uma palavra como parâmetro e conta e exibe a quantidade de ocorrências dessa palavra em um arquivo chamado "busca.txt". Entregue apenas a função.

def acha_palavra(palavra):
    with open("busca.txt") as f:
        conteudo = f.read()
        contagem = conteudo.lower().count(palavra.lower())
        print(f"{contagem}")

def acha_palavra(palavra):
    with open("busca.txt") as f:
        conteudo = f.read()
        palavras = conteudo.split()  # Divide o conteúdo em palavras
        
        contagem = conteudo.lower().count(palavra.lower())
        
        conjuncoes = [p for p in palavras if p.lower() in ['e', 'a', 'o']]  
        
        if palavra in contagem:
            print(f"{contagem}")
        elif palavra in conjuncoes:
            print(f"{conjuncoes}")
        else:
            print("Palavra não encontrada")

def acha_palavra(palavra):
    with open("busca.txt") as f:
        conteudo = f.read()
        palavras = conteudo.split()  # Divide o conteúdo em palavras
        
        contagem = conteudo.lower().count(palavra.lower())
        
        conjuncoes = ['e', 'a', 'o']
        contagem_conjuncoes = sum (p.lower() in conjuncoes for p in palavras)
        
        if palavra in conjuncoes:
            print(f"{contagem_conjuncoes}")
        elif contagem > 0:
            print(f"{contagem}")
        
        if contagem == 0 and palavra not in conjuncoes:
            print("0")

def acha_palavra(palavra):
    with open("busca.txt") as f:
        conteudo = f.read()
        palavras = conteudo.split()  # Divide o conteúdo em palavras
        
        contagem = conteudo.lower().count(palavra.lower())
        
        conjuncoes = ['e', 'a', 'o']
        contagem_conjuncoes = sum(p.lower() in conjuncoes for p in palavras if p.lower() not in ['a', 'e', 'o'])
        
        if palavra in conjuncoes:
            print(f"{contagem_conjuncoes}")
        elif contagem > 0:
            print(f"{contagem}")
        
        if contagem == 0 and palavra not in conjuncoes:
            print("0")
