while True:
    n = int(input('Insira um numero para ver sua tabuada(0 para sair): '))
    if n == 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Fechando programa! ')