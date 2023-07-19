a = input("Digite a letra desejada: ")
if a in {"a", "e", "i", "o", "u"}:
    print ("Essa letra é uma vogal")
elif a in {"y"}:
    print("Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.")
elif a in {"b", "d", "c", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "z"}:
    print("Essa letra é uma consoante.")
else:
    print("Digite uma letra.")