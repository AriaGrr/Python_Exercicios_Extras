#Crie uma função em Python chamada contaPalavras que recebe uma string e que conte a quantidade de incidências de todas as palavras em uma string, assim listando todas as palavras e suas quantidades. Sua função deve  retornar o número de palavras contadas  em formato de dicionário. A função deverá retornar um dicionário referente as palavras encontradas (sem duplicidade) e a quantidade de incidência de cada uma das palavras. Sua função deverá considerar todas as palavras como letras minúsculas, remova também as virgulas e os caracteres "!" e "?".

def contaPalavras(frase):
    frase = frase.lower()
    frase = frase.replace(",", "")
    frase = frase.replace("!", "")
    frase = frase.replace("?", "")
    frase = frase.split()
    d = {}
    for i in frase:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

