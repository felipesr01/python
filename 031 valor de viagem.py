v = float(input('Insira a distancia da viagem: '))
x = 0.50 * v
y = 0.45 * v
if v <= 200.0:
    print(f'Valor da viagem e R${x}')
else:
    print(f'Valor da viagem e R${y}')