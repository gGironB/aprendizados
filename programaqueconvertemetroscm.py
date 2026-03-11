while True:

    try:
        metros = float(input("Digite o valor em metros: "))
        centimetros = metros * 100
        if metros < 0:
            print("Por favor, digite um valor positivo para a medida em metros.")
            continue
        print(f"{metros} metros é igual a {centimetros} centímetros.")
        break
    except ValueError:
        print("Por favor, digite um número válido para a medida em metros.")