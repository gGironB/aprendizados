#while True, envolve o programa inteiro,
# break só aparece no fim do programa = encerrar

while True:
    try:
        num = float(input("Digite um numero: "))
        operacao = input("Escolha uma operação : + - / * ")

        num2 = float(input("Digite outro número: "))
    
        if operacao == "+":
            resultado = num + num2
            print (f"O resultado e : {num} + {num2} {resultado}")

        elif operacao == "-":
            resultado = num - num2
            print(f"O resultado e : {num} - {num2} {resultado}")

        elif operacao == "/":
            resultado = num / num2
            print(f"O resultado e : {num} / {num2} {resultado}")

        elif operacao == "*":
            resultado = num * num2
            print(f"O resultado e : {num} * {num2} {resultado}")
        else:
            print("Operação invalida")

        
        continuar = input("Continuar? S/N ") 
        if continuar == "N":
            break
    except:
        print("Apenas numeros e operações validas! ")
        
