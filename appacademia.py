treinos = []
while True:
    print("1 - Adicionar treino")
    print("2 - Ver treinos")
    print("3 - Sair")
    
    opcao = input("Escolha : ")
    if opcao == "1":
        exercicio = input("Escolha um exercicio: ")
        reps =  int(input("Quantas reps: "))
        peso = int(input("Peso: "))
        treinos.append ([exercicio,reps,peso])
        print("Treino salvo!")
        
    elif opcao == "2":
        if not treinos:
            print("Nenhum treino salvo!")
        else:
            for t in treinos:
                print(t)
            
    elif opcao == "3":
        break
# segunda versao do "aplicativo de academia"
