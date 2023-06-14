def leiaint(msg):
    n = str(input('Digite um numero: '))
    if msg.isnumeric():
        msg = int(n)
    else:
        while msg.isnumeric() is False:
            print('\033[0;31mInvalido, insira um numero.\033[m')
            msg = str(input('Digite um numero: '))
    return msg


n = leiaint('Digite um numero: ')
print(f'Voce digitou o numero {n}')
