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
                    print(f"{i+1} - Exercicio: {t[0]} / Reps: {t[1]} / Peso: {t[2]}")


def remover_treino(treinos):
     if not treinos:
          print("Nenhum treino adicionado!")
          return # "return serve para sair cedo da funcao, no caso desse, visto que nao tem treino para remover, apenas informa o mesmo"
     mostrar_treino(treinos)
     numero = int(input("Qual treino remover?"))
     indice = numero - 1
     if indice >= 0 and indice < len(treinos):
          treinos.pop(indice)     
          print("Treino removido! ")
     else:
          print("Treino invalido! ")

while True:
    print("1 - Adicionar treino")
    print("2 - Ver treinos")
    print("3 - Remover treino")
    print("4 - Sair")
    opcao = input("Escolha : ")

    if opcao == "1":
         adicionar_treino(treinos)
    elif opcao == "2":
         mostrar_treino(treinos)
    elif opcao == "3":
          remover_treino(treinos)
    elif opcao == "4":
     break
    else:
         print("Opção invalida")
    
            
   