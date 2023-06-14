print('Caixa eletronico!')
ced100 = ced50 = ced20 = ced10 = ced5 = ced2 = ced1 = calc = 0
valor = float(input('Qual Valor voce quer sacar?'))
while True:
    while calc < valor:
        calc += 100
        ced100 += 1
    if calc > valor:
        calc -= 100
        ced100 -= 1
    while calc < valor:
        calc += 50
        ced50 += 1
    if calc > valor:
        calc -= 50
        ced50 -= 1
    while calc < valor:
        calc += 20
        ced20 += 1
    if calc > valor:
        calc -= 20
        ced20 -= 1
    while calc < valor:
        calc += 10
        ced10 += 1
    if calc > valor:
        calc -= 10
        ced10 -= 1
    while calc < valor:
        calc += 5
        ced5 += 1
    if calc > valor:
        calc -= 5
        ced5 -= 1
    while calc < valor:
        calc += 2
        ced2 += 1
    if calc > valor:
        calc -= 2
        ced2 -= 1
    while calc < valor:
        calc += 1
        ced1 += 1
    if calc > valor:
        calc -= 1
        ced1 -= 1
    break
print(calc)
print(f'{ced100} Cedulas de R$100')
print(f'{ced50} Cedulas de R$50')
print(f'{ced20} Cedulas de R$20')
print(f'{ced10} Cedulas de R$10')
print(f'{ced5} Cedulas de R$5')
print(f'{ced2} Cedulas de R$2')
print(f'{ced1} Cedulas de R$1')
