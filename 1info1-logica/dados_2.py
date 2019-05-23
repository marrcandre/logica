# Programa dos dados
# Marco André Mendes <marcoandre@gmail.com>

import random

print("Jogo de Dados (v.0.1")

dados1 = random.randint(1, 6)
dados2 = random.randint(1, 6)
jogador1 = dados1 + dados2

dados3 = random.randint(1, 6)
dados4 = random.randint(1, 6)
jogador2 = dados3 + dados4

print("Dado 1:", dados1)
print("Dado 2:", dados2)
print("Dado 3:", dados3)
print("Dado 4:", dados4)

print("Jogador 1: ", jogador1)
print("Jogador 2: ", jogador2)

if jogador1 > jogador2:
    print('Jogador 1 venceu!')
else:
    if jogador2 > jogador1:
        print("Jogador 2 venceu!")
    else:
        print("Empate!")
