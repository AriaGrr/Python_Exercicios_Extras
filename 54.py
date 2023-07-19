#Trata-se de um tipo de substituição, na qual cada letra de um texto a ser criptografado é substituída por outra letra presente no alfabeto, porém deslocada um certo número de posições à esquerda ou à direita. Por exemplo, se empregarmos uma troca de quatro posições à esquerda, cada letra é substituída pela letra que está quatro posições adiante no alfabeto, e nesse caso a letra A seria substituída pela letra E, a letra B por F, a letra C por G, e assim sucessivamente. Crie uma função chamada criptCesar que receba uma frase e o valor do deslocamento, podendo ser positivo ou negativo. A criptografia deverá ser cíclica, como na imagem acima, isso significa que quando terminar em Z o próximo caractere é A. Sua função deve ignorar caracteres especiais e os espaços.

def criptCesar(frase, deslocamento):
    frase = frase.upper()
    list(frase)
    frase_cript = []
    for i in frase:
        if i.isalpha():
            if i.isupper():
                if ord(i) + deslocamento > 90:
                    frase_cript.append(chr(ord(i) + deslocamento - 26))
                elif ord(i) + deslocamento < 65:
                    frase_cript.append(chr(ord(i) + deslocamento + 26))
                else:
                    frase_cript.append(chr(ord(i) + deslocamento))
            else:
                if ord(i) + deslocamento > 122:
                    frase_cript.append(chr(ord(i) + deslocamento - 26))
                elif ord(i) + deslocamento < 97:
                    frase_cript.append(chr(ord(i) + deslocamento + 26))
                else:
                    frase_cript.append(chr(ord(i) + deslocamento))
        else:
            frase_cript.append(i)

    print(''.join(frase_cript))


