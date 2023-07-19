#Embora a popularidade dos cheques como método de pagamento tenha diminuído nos últimos anos, algumas empresas ainda os emitem para pagar funcionários ou fornecedores. A quantia que está sendo paga normalmente aparece duas vezes em um cheque, com uma ocorrência escrita com números e outra ocorrendo com palavras. Repetir o valor em dois formulários diferentes torna muito mais difícil para um funcionário ou fornecedor inescrupuloso modificar o valor do cheque antes de depositá-lo. Neste exercício, sua tarefa é criar uma função (chamada numero_texto) que receba um número inteiro entre 0 e 999 como seu único parâmetro e retorne uma string contendo as palavras em português para esse número. Por exemplo, se o parâmetro para a função for 142, sua função deve retornar “cento e quarenta e dois”. Use um ou mais dicionários para implementar sua solução, em vez de grandes construções if / elif / else. 

d = {0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte", 21: "vinte e um", 22: "vinte e dois", 23: "vinte e três", 24: "vinte e quatro", 25: "vinte e cinco", 26: "vinte e seis", 27: "vinte e sete", 28: "vinte e oito", 29: "vinte e nove", 30: "trinta", 40: "quarenta", 50: "cinquenta", 60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa", 100: "cento", 200: "duzentos", 300: "trezentos", 400: "quatrocentos", 500: "quinhentos", 600: "seiscentos", 700: "setecentos", 800: "oitocentos", 900: "novecentos"}

def numero_texto(n):
    if n == 100: 
        print ("cem")
    elif n in d:
        print(d[n])
    elif n > 100 and n < 1000:
        centena = n // 100
        dezena = (n % 100) // 10
        unidade = (n % 100) % 10
        if dezena == 0:
            print(d[centena * 100], "e", d[unidade])
        elif dezena == 1:
            print(d[centena * 100], "e", d[unidade + 10])
        elif unidade == 0:
            print(d[centena * 100], "e", d[dezena * 10])
        else:
            print(d[centena * 100], "e", d[dezena * 10], "e", d[unidade])
    elif n > 30 and n < 100:
        dezena = n // 10
        unidade = n % 10
        if unidade == 0:
            print(d[dezena * 10])
        else:
            print(d[dezena * 10], "e", d[unidade])
    else:
        print("Número inválido.")

n = int(input("Digite um número entre 0 e 999: "))
numero_texto(n)
