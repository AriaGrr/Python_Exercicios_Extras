#Faça um jogo da forca: O jogo deve começar solicitando a palavra secreta para o usuário 1 (o usuário 1 pode entrar com letras maiúsculas ou minúsculas, isto não deve influenciar no jogo). Então, o usuário 2, deve chutar as letras da palavra secreta e tentar acertá-la. Lembre-se de que o usuário 2 não deve poder ver a palavra secreta digitada pelo usuário 1. O usuário 2 pode errar a letra 5 vezes. No sexto erro, o jogo termina.  O jogo deve verificar se a letra digitada pelo usuário 2 já foi ou não digitada. Letras repetidas não devem contar. O jogo deve também mostrar a quantidade de letras da palavra secreta, assim como as letras corretas em suas devidas posições.usuário 1: O usuário 2 vê a seguinte tela, onde cada “-” representa uma letra da palavra secreta: Se o usuário 2 errar, a seguinte tela aparece: Se o usuário 2 acertar, a letra é exibida no(s) lugar(es) correto(s) da palavra secreta: A cada erro, o “enforcado” deve ir ganhando forma.

a = input("Digite a palavra secreta:")
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
a = a.lower()
b = []
for i in a:
    b.append(i)
c = []
for i in range(len(b)):
    c.append("-")
print("".join(c))
d = []
e = 0
while e < 6:
    print()
    f = input("Digite uma letra:")
    f = f.lower()
    if f in d:
        print("Letra já digitada!")
    else:
        d.append(f)
        if f in b:
            for i in range(len(b)):
                if f == b[i]:
                    c[i] = f
            print("X==:==\nX  :  \nX    \nX  \nX   \nX\n===========")
            print("".join(c))
        else:
            e += 1
            print("Você errou!")
            if e == 1:
                print("X==:==\nX  :  \nX  O  \nX  \nX   \nX\n===========")
                print("".join(c))
            elif e == 2:
                print("X==:==\nX  :  \nX  O  \nX  |\nX   \nX\n===========")
                print("".join(c))
            elif e == 3:
                print("X==:==\nX  :  \nX  O  \nX \|\nX   \nX\n===========")
                print("".join(c))
            elif e == 4:
                print("X==:==\nX  :  \nX  O  \nX \|/\nX   \nX\n===========")
                print("".join(c))
            elif e == 5:
                print("X==:==\nX  :  \nX  O  \nX \|/\nX /  \nX  \n===========")
                print("".join(c))
            elif e == 6:
                print("X==:==\nX  :  \nX  O  \nX \|/\nX / \  \nX \n===========")    
                print("Enforcado!")
                break
    if "-" not in c:
        print("Você acertou!")
        break

