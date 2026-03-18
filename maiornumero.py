n1 = int(input("DIGITE UM NUMERO: "))
n2 = int(input("DIGITE OUTRO NUMERO: "))
n3 = int(input("DIGITE MAIS UM NUMERO: "))

def numero_maior (n1,n2,n3):
    numeros = n1, n2, n3
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
x = numero_maior (n1,n2,n3)
print (f"O maior numero e {x}")