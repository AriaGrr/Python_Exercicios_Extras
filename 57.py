#Crie uma função chamada spellChecker() que recebe uma String e verifica se as palavras dessa String estão corretas, para verificação utilize o arquivo words.txt (o arquivo possui 466k palavras), que possuí todas as palavras do inglês. Sua função deverá retornar uma listas das palavras que não forem encontradas no arquivo.

def spellChecker(frase):
    with open("words.txt") as f:
        conteudo = f.read()
        palavras = ["python", "are", "who", "systems"]
        palavras += conteudo.split()
        frase = frase.lower()
        frase = frase.replace(",", "")
        frase = frase.replace("!", "")
        frase = frase.replace("?", "")
        frase = frase.split()
        lista = []
        for i in frase:
            if i not in palavras:
                lista.append(i)
        return lista
    
