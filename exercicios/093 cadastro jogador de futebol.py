jogador = {'nome': '', 'gols': [], 'total': 0}
jogador['nome'] = str(input('Nome do Jogador: ')).title()
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
totgols = 0

for c in range(0, part):
    golsp = int(input(f'Quantos gols na partida {c+1}? '))
    totgols += golsp
    jogador['gols'].append(golsp)
    jogador['total'] = totgols
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   =>Na {i+1}º partida, fez {v} gols')
print(f'Total de gols: {jogador["total"]}')
