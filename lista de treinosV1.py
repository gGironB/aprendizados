
treinos = []
while True:
    exercicio = input("Digite o exercicio :")
    reps = int(input("Digite as repetições :"))
    peso = float(input("Digite o peso :"))
    treinos.append([exercicio, reps, peso])
    for t in treinos:
        print(t)
    sair = input("Continuar? S/N?")
    if sair.lower() == "n":
        break