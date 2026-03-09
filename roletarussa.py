if input("Roleta russa, voce quer jogar? (s/n) ") == "s":
    print("Vamos jogar!")
else:
    print("Você não tem escolha, vamos jogar!")

import random 
balas = [0,0,0,0,0,0,1]
random.shuffle(balas)
for i in range(6):
    input("Gire o tambor e aperte o gatilho: ")
    if balas[i] == 1:
        print("BANG! Você morreu.")
        break
    else:
        print("Click! Você sobreviveu.")
if i == 5:
    print("Parabéns! Você sobreviveu a roleta russa!")
