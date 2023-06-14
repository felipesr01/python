import random
import time

lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
user = str(input('Pedra, papel ou tesoura? ')).lower().strip()
print('-'*13)
print('Pe',end= '')
time.sleep(0.5)
print('dra')
time.sleep(1)
print('Papel')
time.sleep(1)
print('Te', end= '')
time.sleep(1)
print('soura')
print('-'*13)
print(f'Voce escolheu {user} e o programa escolheu {pc}')
if pc == user:
    print('empate!')
elif (user == 'pedra' and pc == 'tesoura') or (user == 'tesoura' and pc == 'papel') or (user == 'papel' and pc == 'pedra'):
    print('Venceu!')
else:
    print('Voce perdeu!')
