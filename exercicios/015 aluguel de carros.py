kmc = float(input('Quantos Km rodados?: '))
diac = int(input('Quantos dias alugado?: '))

calckm = kmc * 0.15
calcd = diac * 60
total = calcd + calckm

print(f'Voce dirigiu por {kmc}Km e por {diac} dias')
print(f'O valor total sera de {total}')
