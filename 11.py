a = input("Digite a nota em letra, e o sinal +/-: ")
if a in {"A+", "A"}:
    print("%s é equivalente a 5.0" %(a))
elif a == "A-":
    print ("A- é equivalente a 4.5")
elif a == "B+":
    print ("B+ é equivalente a 4.0")
elif a == "B":
    print ("B é equivalente a 3.5")
elif a == "B-":
    print ("B- é equivalente a 3.0")
elif a == "C+":
    print ("C+ é equivalente a 2.5")
elif a == "C":
    print ("C é equivalente a 2.0")
elif a == "C-":
    print ("C- é equivalente a 1.5")
elif a == "D+":
    print ("D+ é equivalente a 1.0")
elif a == "D":
    print ("D é equivalente a 0.5")
elif a == "F":
    print ("F é equivalente a 0.0")
else:
    print("Nota inválida")