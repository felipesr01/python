import random
import time

comp = random.randint(0,10)
tent = 1
print('Pensei em um numero de 0 a 10')
time.sleep(1)
print('Consegue advinhar?')
user = int(input('Seu chute: '))
while user != comp:
    if user > comp:
        tent += 1
        user = int(input('Chute mais baixo! '))
    elif user < comp:
        user = int(input('Chute mais alto! '))
        tent += 1
if user == comp:
    print(f'Voce acertou com {tent} tentativas')