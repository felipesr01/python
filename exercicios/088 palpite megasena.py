from random import randint
from time import sleep
lista = []
jogos = []
total = 1
perg = int(input('Quantos jogos voce quer sortear? '))
while total <= perg:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Sorteando {total} jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('Boa sorte')
