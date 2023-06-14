valores = []
while True:
    v = int(input('Digite um Valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso')
    else:
        print('Valor ja adicionado!')
    op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        break
valores.sort()
print(f'Voce digitou os valores {valores}')
