#Crie uma função em Python chamada contaPalavras que recebe uma string e conta quantas palavras tem nessa string. Sua função deve  retornar o número de palavras contadas. 

def contaPalavras(frase):
    frase = frase.lower()
    frase = frase.replace(",", "")
    frase = frase.replace("!", "")
    frase = frase.replace("?", "")
    frase = frase.split()
    return len(frase)

