#Um dicionário pode ser utilizado para representar um estoque de uma empresa. Nele, todos os itens de uma empresa são registrados, anotando a quantidade de itens disponíveis e o seu valor unitário.Faça um programa que permita gerenciar um estoque de uma Quitanda. O programa deve permitir inserir itens no estoque, remover itens, modificar a quantidade e preço de um item e imprimir todo o estoque. Faça este programa usando funções e dicionários.

dicionario = {'maça': {'Quantidade': 100, 'Preco': 1.5} , 'banana': {'Quantidade': 12, 'Preco': 3.2} }

def inserirItem():
    item = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade do item: "))
    preco = float(input("Digite o preço do item: "))
    dicionario[item] = {'Quantidade': quantidade, 'Preco': preco}

def removerItem():
    item = input("Digite o nome do item: ")
    if item in dicionario:
        del dicionario[item]
    else:
        print("Item não encontrado!")

def modificarQuantidade():
    item = input("Digite o nome do item: ")
    if item in dicionario:
        quantidade = int(input("Digite a nova quantidade do item: "))
        dicionario[item]['Quantidade'] = quantidade
    else:
        print("Item não encontrado!")

def modificarPreco():
    item = input("Digite o nome do item: ")
    if item in dicionario:
        preco = float(input("Digite o novo preço do item: "))
        dicionario[item]['Preco'] = preco
    else:
        print("Item não encontrado!")

def imprimirEstoque():
    print(dicionario)

def menu():
    print("1 - Inserir item")
    print("2 - Remover item")
    print("3 - Modificar quantidade")
    print("4 - Modificar preço")
    print("5 - Imprimir estoque")
    print("6 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

opcao = menu()
while opcao != 6:
    if opcao == 1:
        inserirItem()
    elif opcao == 2:
        removerItem()
    elif opcao == 3:
        modificarQuantidade()
    elif opcao == 4:
        modificarPreco()
    elif opcao == 5:
        imprimirEstoque()
    else:
        print("Opção inválida!")
    opcao = menu()

print("Fim do programa!")

