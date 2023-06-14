n = int(input('Tabuada de: '))

com = int(input('Comecar em: '))
fim = int(input('Terminar em: '))
while fim < com:
    fim = int(input('Final nao pode ser menor que inicial: '))
for c in range(com, (fim+1)):
    print(f'{n} x {com} = {n*com}')
    com += 1