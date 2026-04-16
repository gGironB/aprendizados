treinos = []

def adicionar_treino(treinos):
     while True:
          try: 
               exercicio = input("Escolha um exercicio: ")
               reps =  int(input("Quantas reps: "))
               peso = int(input("Peso: "))
               treinos.append ([exercicio,reps,peso])
               print("Treino salvo!")
               break
          except:
               print("apenas informacoes validas")     
     


def mostrar_treino(treinos):
        
          
          
        if not treinos:
            print("Nenhum treino salvo!")
        else:
               for i, t in enumerate(treinos):
                    print(f"{i+1} - Exercicio: {t[0]} / Reps: {[1]} / Peso: {[2]}")

while True:
    print("1 - Adicionar treino")
    print("2 - Ver treinos")
    print("3 - Sair")
    opcao = input("Escolha : ")

    if opcao == "1":
         adicionar_treino(treinos)
    elif opcao == "2":
         mostrar_treino(treinos)
    elif opcao == "3":
         break
    else:
         print("Opção invalida")
    
            
   