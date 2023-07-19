a = int(input("Digite o dia desejado: "))
b = input("Digite o mês desejado: ")

if b in { "janeiro", "fevereiro"}:
    print ("Verão")
elif b in {"abril", "maio"}:
    print ("Outono")
elif b in {"julho", "agosto"}:
    print ("Inverno")
elif b in {"outubro", "novembro"}:
    print ("Primavera")

elif b in {"março"} and a in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}:
    print ("Verão")
elif b in {"junho"} and a in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}:
    print ("Outono")
elif b in {"setembro"} and a in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}:
    print ("Inverno")
elif b in {"dezembro"} and a in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}:
    print ("Primavera")

elif b in { "março"} and a in {20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}:
    print ("Outono")
elif b in {"junho"} and a in { 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}:
    print ("Inverno")
elif b in {"setembro"} and a in { 22, 23, 24, 25, 26, 27, 28, 29, 30}:
    print ("Primavera")
elif b in {"dezembro"} and a in { 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}:
    print ("Verão")

else:
    print ("Digite um mês e dia validos.")