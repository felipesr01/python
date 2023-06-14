num = int(input('Numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        tot += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n')
print(f'\033[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print("É primo")
else:
    print('Nao é primo')
