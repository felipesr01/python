lista = []
listai = []
listap = []
'''
#colocando na hora q digita
while True:
    v = int(input('Insira um valor: '))
    lista.append(v)
    if v % 2 == 0:
        listap.append(v)
    elif v % 2 != 0:
        listai.append(v)
    op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        break
print(f'Lista: {lista}')
print(f'Lista de Pares: {listap}')
print(f'Lista de Impares: {listai}')
'''

#criando a lista e a partir dela criando as outras
c = 0
while True:
    v = int(input('Insira um valor: '))
    lista.append(v)
    c += 1
    op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        break
for cont, n in enumerate(lista):
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)


print(f'Lista: {lista}')
print(f'Lista de Pares: {listap}')
print(f'Lista de Impares: {listai}')