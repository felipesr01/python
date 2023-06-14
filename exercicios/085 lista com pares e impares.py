num = [[], []]
for c in range(1, 8):
    n = int(input(f'Insira o {c}º numero: '))
    if n % 2 != 0:
        num[1].append(n)
    else:
        num[0].append(n)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')