
def combinaStrings(string1, string2):
    if len(string1) > len(string2):
        maior = string1
        menor = string2
    else:
        maior = string2
        menor = string1
    for i in range(len(menor)):
        print(string1[i] + string2[i], end="")
    print(maior[len(menor):])


def main():
    string1 = str(input(''))
    string2 = str(input(''))
    combinaStrings(string1, string2)
    