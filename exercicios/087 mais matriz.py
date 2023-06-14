matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = somac = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Insira um valor para [{l}, {c}]: '))
        #pegando pares
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        #somando 3 coluna
        if c == 2:
            somac += matriz[l][c]
#escrevendo a matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end='')
    print()

print(f'Soma dos pares: {pares}')
print(f'Soma Terceira coluna: {somac}')
#pegando maior da segunda linha
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'Maior da segunda linha {maior}')
