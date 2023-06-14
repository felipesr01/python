lista = ('lapis', 1.75,
         'borracha', 2.00,
         'caderno', 15.90,
         'estojo', 25.00,
         'transferidor', 4.20,
         'compasso', 9.99,
         'mochila', 120.32,
         'canetas', 22.30,
         'livro', 34.90)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>8.2f}')
