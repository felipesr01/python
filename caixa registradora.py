cont = 1
soma = 0

print('Digite 0 para parar!')
while True:
    prod = float(input(f'Produto {cont}: '))
    if prod == 0:
        break
    cont += 1
    soma += prod
din = float(input('Dinheiro: '))
while din < soma:
    din = float(input('Valor a ser pago é menor que o total da compra: '))
troco = din - soma
print(f'Total: R$ {soma}')
print(f'Troco: R$ {troco}')