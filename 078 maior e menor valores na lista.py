
valores = []
for v, c in enumerate(range(0, 5)):
    valores.append(int(input(f'Digite o valor para a posicao {v}: ')))
print(f' Voce digitou os valores {valores}')
print(f'O menor valor digitado foi {min(valores)}, nas posicoes ', end=' ')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...',end='')
print()
print(f'O maior valor digitado foi {max(valores)}, nas posicoes ', end=' ')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')
print()
