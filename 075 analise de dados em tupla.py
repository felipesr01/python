n1 = int(input('Insira um numero: '))
n2 = int(input('Insira outro numero: '))
n3 = int(input('Insira mais um numero: '))
n4 = int(input('Insira o ultimo numero: '))
lista = (n1, n2, n3, n4)

if 3 in lista:
    p3 = lista.index(3)
    print(f'Posicao do 3: {p3+1}')
else:
    print('Nao foi digitado nenhum numero 3')
cont = lista.count(9)
print(f'Numeros 9: {cont}')

print('Numeros pares: ',end='')
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        print(lista[c], end=' ')