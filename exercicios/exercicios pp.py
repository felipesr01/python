'''
maior = 0
menor = 0
for c in range(1,6):
    n = int(input(f'Insira o {c} numero: '))
    if n == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'O maior numero digitado foi {maior}, o menor foi {menor}')
'''
