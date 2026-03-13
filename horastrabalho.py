#programa que calcula valor do dia trabalhado



while True:
    try:
        salario = float(input("Quanto e o seu salario: "))
        dias = int(input("Quantos dias trabalhados?: "))

        resultado = salario / dias

        print (f"O seu dia vale R${resultado:.2f} ")
        break
    except:
        print("Apenas numeros validos")