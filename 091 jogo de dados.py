from random import randint
from time import sleep
jogos = {}
jogos['Jogador1'] = randint(1, 6)
jogos['Jogador2'] = randint(1, 6)
jogos['Jogador3'] = randint(1, 6)
jogos['Jogador4'] = randint(1, 6)
print('Valores sorteados:')
for k, v in jogos.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores: ')
for i in sorted(jogos, key=jogos.get, reverse=True):
    print(i, jogos[i])