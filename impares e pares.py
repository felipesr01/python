par = impar = 0
for c in range(0, 10):
    n = int(input(f'Insira o {c+1}º numero: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Impares: {impar}')
print(f'Pares: {par}')
