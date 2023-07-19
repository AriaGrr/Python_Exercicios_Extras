A = int(input("Digite o valor do primeiro produto: "))
B = int(input("Digite o valor do segundo produto: "))
C = int(input("Digite o valor do terceiro produto: "))
total = float(A + B + C)
if total >= 500:
    print("Desconto: %.2f" %(total * 0.2))
else:
    print("Desconto: %.2f" %(total * 0.1))