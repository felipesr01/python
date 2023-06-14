def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).title()
if nome == '':
    nome = '<desconhecido>'

gols = str(input('Quantos gols ele fez? '))
if gols.isnumeric():
    gols = gols
else:
    gols = 0
ficha(nome, gols)
