prim = int(input('Primeiro termo: '))
raz = int(input('Razao: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += raz
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais? '))
print('Fim')
print(f'Foram mostrados {total} termos')