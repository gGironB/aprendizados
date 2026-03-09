#programa que verifica se um número é inteiro

num = input("Digite um número: ")

if num.isdigit():
    num = float(num)
    if num >= 1:
        print("O número é positivo.")
    elif num < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")
else:
    print("Apenas números.")
