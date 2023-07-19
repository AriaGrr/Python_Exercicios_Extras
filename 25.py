#Sua função deverá receber entre 3 e 6 parâmetros e retornar o valor do produtório. Não é necessário fazer o programa principal.

def produtorio(*args):
    prod = 1
    for i in args:
        prod *= i
    return prod


