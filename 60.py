#Construa um programa em Python que deve receber duas strings e combiná-las, alternando uma letra de cada string em uma palavra resultante (que será diretamente exibida na tela, não é salva em uma variável). Considere que uma string pode ser maior que a outra na entrada; nesse caso, as letras que sobrarem (não utilizadas durante a alternância) devem ser adicionadas ao fim da palavra resultante.

def combinaStrings(string1, string2):
    if len(string1) > len(string2):
        maior = string1
        menor = string2
    else:
        maior = string2
        menor = string1
    for i in range(len(menor)):
        print(string1[i] + string2[i], end="")
    print(maior[len(menor):])

def main():
    string1 = str(input(''))
    string2 = str(input(''))
    combinaStrings(string1, string2)
    
main()