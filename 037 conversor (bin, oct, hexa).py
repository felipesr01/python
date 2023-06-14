num = int(input('Insira um numero inteiro: '))
print('''Escolha uma das opcoes para converter
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL)''')
op = int(input('Sua opcao: '))

if op == 1:
    print(f'{num} convertido para binario e {bin(num)[2:]}')
elif op == 2:
    print(f'{num} convertido para octal e {oct(num)[2:]}')
elif op == 3:
    print(f'{num} convertido para hexadecimal e {hex(num)[2:]}')
else:
    print('Insira um numero valido')