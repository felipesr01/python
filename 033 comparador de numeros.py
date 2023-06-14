n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o ultimo numero: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} e o maior')
elif n2 > n1 and n2 > n3:
    print(f'{n2} e o maior')
elif n3 > n1 and n3 > n2:
    print(f'{n3} e o maior')
else:
    print('Todos sao iguais')