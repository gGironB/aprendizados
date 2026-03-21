while True:
    try:
        n1 = float(input("digite um numero : "))
        n2 = float(input("digite outro numero : "))
        break
    except:
        print("Apenas numeros")
        
operacao = input("escolha operacao (+ - / *):  ")
def numeros_cal(n1,n2,operacao):
    

    if operacao == ("+"):
        return n1 + n2
        
    elif operacao == ("-"):
        return n1 - n2
    
    elif operacao == ("/"):
        if n2 == 0:
            return "erro"
        else: 
            return n1 / n2
    elif operacao == ("*"):
        return n1 * n2
    else:
        return "erro de operacao"
resultado = numeros_cal(n1, n2, operacao)
print("seu resultado é :", resultado)
        
