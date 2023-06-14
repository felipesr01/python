n = int(input('Digire um numero [0 para parar]: '))
cont = 0
soma = 0
while n != 0:
    cont += 1
    soma += n
    n = int(input('Digire um numero [0 para parar]: ')) #se colocar o n como a ultima linha, o 0 nao vai ser contado
print(f'Voce digitou {cont} numeros e a soma foi de {soma}')