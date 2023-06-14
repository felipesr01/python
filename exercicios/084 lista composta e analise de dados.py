dado = []
pessoas = []
mai = men = 0
while True:
    n = dado.append(str(input('Nome: ')))
    p = dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    perg = str(input('Quer continuar? [S/N] ')).lower().strip()
    while perg not in 'sn':
        perg = str(input('[S/N]: '))
    if perg == 'n':
        break
print(pessoas)
print(f'Pessoas cadastradas: {len(pessoas)}')
print(f'O peso maior foi de {mai}. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == mai:
        print(f'[{pessoa[0]}]', end='')
print()
print(f'O peso menor foi de {men}. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == men:
        print(f'[{pessoa[0]}]', end='')
