s = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'{c} Valor: '))
    if num % 2 == 0:
        s += c
        cont += 1
print(f'Numeros pares: {cont}')
print(f'Soma dos numeros {s}')
