import random
n = random.randint(0, 5)
nu = int(input('Adivinhe o numero de 0 a 5: '))
if nu != n:
    print('Errou!')
    print(f'Eu pensei em {n} nao em {nu}')
else:
    print('Acertou!')