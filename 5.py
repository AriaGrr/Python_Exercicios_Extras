a = str.capitalize(input(""))
if a == "Fevereiro":
    print ("28 ou 29 dias")
elif a == "Abril" or  a == "Junho" or  a == "Setembro" or  a == "Novembro":
    print ("30 dias")
elif a == "Março" or  a == "Janeiro" or  a == "Maio" or  a == "Julho" or  a == "Agosto" or  a == "Outubro" or  a == "Dezembro":
    print ("31 dias")
else: 
    print("Mês invalido.")