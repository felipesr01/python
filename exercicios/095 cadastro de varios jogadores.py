time = []
while True:
    jogador = {'nome': '', 'gols': [], 'total': 0}
    jogador['nome'] = str(input('Nome do Jogador: ')).title()
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    totgols = 0

    for c in range(0, part):
        golsp = int(input(f'Quantos gols na partida {c + 1}? '))
        totgols += golsp
        jogador['gols'].append(golsp)
    jogador['total'] = totgols
    time.append(jogador.copy())
    op = str(input('Quer continuar? [S/N] '))
    while op not in 'sn':
        op = str(input('[S/N]'))
    if op == 'n':
        break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    perg = int(input('Quer ver o levantamento de qual jogador? (negativo encerra): '))
    if perg < 0:
        break
    if perg >= (len(time)):
        print(f'Nao existe jogador com codigo {perg}: ')
    else:
        print(f'Levantamento do jogador {time[perg]["nome"]}')
        for i, g in enumerate(time[perg]['gols']):
            print(f'     No jogo {i+1} fez {g} gols')
    print('-'*40)
print('Encerrando.')