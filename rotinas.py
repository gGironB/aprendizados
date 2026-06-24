rotina =  []
while True:
    horario = input("Digite o horario: ")
    atividade = input("Digite a atividade: ")
    teste = { 
    "horario" : horario, "atividade" : atividade
    }
    rotina.append(teste)
    continuar = input("Deseja continuar? S/N: ")
    if continuar.lower() == "s":
        print("Adicionado")
    elif continuar.lower() == "n":
        print("Salvo!")
        break
    else:
        print("Apenas S/N")
for x in rotina:
    print(x["horario"], x["atividade"])
    

    
    