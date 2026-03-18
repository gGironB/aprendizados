# estudo de def/função.

n1 = float(input("DIGITE O PRIMEIRO NUMERO: "))
n2 = float(input("DIGITE O SEGUNDO NUMERO: "))
n3 = float(input("DIGITE O TERCEIRO NUMERO: "))
def conta_media (n1,n2,n3):
    resultado = n1 + n2 + n3
    resultado2 = resultado / 3
    return resultado2
x = conta_media (n1,n2,n3)
print(x)


