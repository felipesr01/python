import random
#66
'''
quant = 0
n = s = 0
while True:
    n = int(input('Numero: '))
    if n == 0:
        break
    s += n
    quant += 1
print(f'Digitou {quant} numeros, a soma vale {s}')


#67
while True:
    n = int(input('Insira um numero para ver sua tabuada: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Fechando programa! ')
'''

#68
venc = 0
user1 = ' '
while True:
    while user1 not in 'pi':
        user1 = str(input('Impar ou par? ')).strip().lower()[0]
    user2 = int(input('Numero: '))
    pcn = random.randint(0,10)
    soma = user2 + pcn
    print(f'Voce jogou {user2} e o computador {pcn}. A soma foi {soma}. Deu', end=' ')
    print('PAR' if soma %2 == 0 else 'IMPAR')
    if user1 in 'p':
        if soma % 2 == 0:
            print('Voce Venceu!')
            user1 = ' '
            venc += 1
        else:
            print(f'Perdeu, voce ganhou {venc} vezes seguinhas')
            break
    if user1 in 'i':
        if soma % 2 != 0:
            print('Voce Venceu!')
            user1 = ' '
            venc += 1
        else:
            print(f'Perdeu, voce ganhou {venc} vezes seguidas')
    print('Vamos jogar de novo!')
print('Fechando jogo...')