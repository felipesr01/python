v = float(input('Insira velocidade: '))
ex = v - 80
m = 7 * ex
if v > 80.0:
    print('Multado!')
    print(f'Estava a {ex}km/h acima do limite, pagara R${m}')
else:
    print('Nao foi multado.')