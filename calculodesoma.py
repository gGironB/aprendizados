
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é: {resultado}")
except:
    print("Por favor, digite apenas números válidos.")



#O que o try faz
#Ele basicamente diz para o Python:
#tente executar isso
#se algo der errado, não quebre o programa
#faça outra coisa