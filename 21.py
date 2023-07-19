#Escreva uma função que tenha os comprimentos dos dois lados mais curtos de um triângulo retângulo como seus parâmetros. Retorne a hipotenusa do triângulo, calculada usando o teorema de Pitágoras, como o resultado da função. Inclua um programa principal que lê os comprimentos dos lados mais curtos de um triângulo retângulo do usuário e use sua função para calcular o comprimento da hipotenusa. Exiba o resultado.


a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = (a**2 + b**2)**0.5
print(f"Hipotenusa: {c :.2f}")


