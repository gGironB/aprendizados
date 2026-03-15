while True:
    try:
        num = float(input("Digite um numero: "))
        operação = input("Escolha a operação : + - * / ")
        num2 = float(input("Digite outro numero: "))
        

        if operação == "+":
            resultado = num + num2
            print(f"resultado {num}+{num2}= {resultado}")
        elif operação == "*":
            resultado = num * num2
            print(f"resultado {num}*{num2}= {resultado}")
        elif operação == "-":
            resultado = num - num2
            print(f"resultado {num}-{num2}= {resultado}")
        elif operação == "/":
            resultado = num / num2
            print(f"resultado {num}/{num2}= {resultado}")
        else:
            print("Apenas operações validas")
    except:
        print("apenas operacoes validas")
