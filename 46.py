#Neste exercício, você simulará 1.000 lançamentos de dois dados. Comece escrevendo uma função que simula o lançamento de um par de dados de seis lados cada. Sua função não deve aceitar nenhum parâmetro. Ela retornará a somatória obtida pelos dois dados. Escreva um programa principal que use sua função para simular 1.000 lançamentos de dois dados. Como acontece em alguns programas, você deve contar o número de vezes que cada somatória acontece. Em seguida, a função principal deve exibir uma tabela que resume esses resultados. Mostre a frequência para cada resultado como uma porcentagem do número total de lançamentos. Use Dicionários.

from random import randint

def lancamento():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    return d1 + d2

def main():
    d = {}
    for i in range(1000):
        l = lancamento()
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    for i in d:
        print("A soma {} ocorreu {} vezes, {:.2f}%".format(i, d[i], d[i] / 1000 * 100))

main()