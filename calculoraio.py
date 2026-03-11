while True:
 try:    
    raio = float(input("Digite o raio do círculo: "))
    resposta = 3.1415 * raio**2
    print(f"A área do círculo é: {resposta}")
    break
 except:
        print("apenas numeros validos")