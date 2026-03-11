while True:# Loop infinito para garantir que o usuário digite números válidos

    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 + n2
        print(f"A soma de {n1} e {n2} é: {resultado}")
        break
    except:
        print("Por favor, digite apenas números válidos.")
