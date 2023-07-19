valor = float(input("Digite o valor da compra: "))
parcela = float(input("Digite a quantidade de parcelas: "))

if valor >= 5000:
    desconto1 = valor * 0.05
else: 
    desconto1 = 0

if parcela == 1:
    desconto2 = valor * 0.1
elif parcela == 2:
    desconto2 = valor * 0.05
elif parcela == 3:
    desconto2 = valor * 0.05
else:
    desconto2 = 0

desconto = desconto1 + desconto2

print("Desconto total: %.2f" %(desconto))
print("Valor final da compra com desconto: %.2f" %(valor - desconto))
print("Cada parcela será de: %.2f" %((valor - desconto)/ parcela))