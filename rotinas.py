rotina =  []

def adicionar_rotina(rotina):
    horario = input("Digite o horario: ")
    atividade = input("Digite a atividade: ")
    teste = { 
        "horario" : horario, "atividade" : atividade
    }
    rotina.append(teste)
    print("Adicionado!")

def mostrar_rotina(rotina):
    if not rotina:
        print("A rotina está vazia.")
        return
    else:
        for i, t in enumerate(rotina):
            print(f"{i+1} - horario: {t['horario']} - atividade: {t['atividade']}")
def remover_rotina(rotina):
    if not rotina:
        print("Nada salvo!")
        return
    else:
        mostrar_rotina(rotina)
    delete =  int(input("Qual remover!"))
    indice = delete - 1
    if indice >= 0 and indice < len(rotina):
        rotina.pop(indice)
        print("Removido!")
    else:
        print("invalido")
    
while True:
    print("1 - Adicionar rotina")
    print("2 - Mostrar rotina")
    print("3 - Excluir")
    print("4 - Fechar")
    opcao = input("Escolha uma opção:")
    if opcao == "1":
        adicionar_rotina(rotina)
    elif opcao =="2":
        mostrar_rotina(rotina)
    elif opcao == "3":
        remover_rotina(rotina)
    else:
        break
