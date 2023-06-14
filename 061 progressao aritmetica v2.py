prim = int(input('Primeiro termo: '))
raz = int(input('Razao: '))
termo = prim
cont = 1
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += raz
    cont += 1
print('Fim')