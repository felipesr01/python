from random import randint


def sorteia(lista):
    print('Lista: ')
    for cont in range(0, 5):
        n = (randint(1, 10))
        lista.append(n)
        print(f'{n} ', end='')


def somap(lista):
    pares = 0
    for n in lista:
        if n % 2 == 0:
            pares += n
    print(f'Soma Pares: {pares}')


numeros = []
sorteia(numeros)
print()
somap(numeros)
