eleitores = int(input('Insira o Total de eleitores: '))

bol = 0
lu = 0
tir = 0
cont = 0
print('CANDITATOS')
print('''[1] BOLSONARO
[2] LULA
[3] TIRIRCA''')
for c in range(1, (eleitores + 1)):
    voto = ' '
    while voto != 1 and voto != 2 and voto != 3:
        voto = int(input(f'Insira o voto da {c}º pessoa: '))
    if voto == 1:
        bol += 1
    elif voto == 2:
        lu += 1
    elif voto == 3:
        tir += 1
    cont += 1
    maior = bol
print(f'Votos Bolsonaro: {bol}')
print(f'Votos Lula: {lu}')
print(f'Votos Tiririca: {tir}')