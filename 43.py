#Faça uma função chamada converte() que recebe um dicionário (dicionário criado pelo Moodle, sempre com o nome codigo_morse)  e uma String contendo uma frase e retorne uma frase convertida em código Morse. Sua função deverá traduzir cada letra e número para o código Morse, deixando um espaço entre cada letra ou número. Sua função deverá ignorar qualquer caractere que não seja letra ou número.

codigo_morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'}

def converte(codigo_morse, frase):
    frase = frase.upper()
    frase = frase.split()
    morse_frase = []  # Lista para armazenar as traduções em código Morse
    
    for i in frase:
        for j in i:
            if j in codigo_morse:
                morse_frase.append(codigo_morse[j])  # Adiciona a tradução à lista
    
    return ' '.join(morse_frase)  # Retorna a lista de traduções como uma string, unindo-as com espaço

                
