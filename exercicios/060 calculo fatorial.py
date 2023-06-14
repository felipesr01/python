n = int(input('Insira o Numero: '))
cont = n
fat = 1
print(f'Calculando {n}!')
while cont > 0:
    print(f'{cont}', end=' ')
    print('x' if cont > 1 else '=', end=' ')
    fat *= cont
    cont -= 1
print(fat)
