n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
sair = 4
while sair != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Numeros
[5] Sair\n''')
    op = int(input('O que deseja fazer? '))
    if op == 1:
        print(f'A soma de {n1} + {n2} = {n1+n2}')
    elif op == 2:
        print(f'A multiplicacao de {n1} x {n2} = {n1*n2}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} maior que {n2}')
        elif n2 > n1:
            print(f'{n2} maior que {n1}')
        elif n1 == n2:
            print('Numeros iguais')
    elif op == 4:
        n1 = int(input('Insira o novo primeiro valor: '))
        n2 = int(input('Insira o novo segundo valor: '))
    elif op == 5:
        print('Saindo')
        sair += 1