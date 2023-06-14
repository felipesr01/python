valores = []
c = 0
while True:
    v = int(input('Insira um valor: '))
    valores.append(v)
    c += 1
    op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        break
print(f'Lista: {valores}')
print(f'Numeros digitados {c}') #ou usar len(valores)
print(f'Lista decrescente: {sorted(valores, reverse=True)}')
if 5 not in valores:
    print('5 nao esta na lista')
else:
    print(f'5 esta na lista, na posicao {valores.index(5)}')
