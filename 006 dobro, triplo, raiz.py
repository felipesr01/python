numero = int(input('Insira um numero: '))
d = numero * 2
t = numero * 3
r = numero ** (1/2)
print(f'Numero: \033[7m{numero}\033[m\nDobro: {d}\nTriplo: {t}\nRaiz Quadrada: {round(r, 2)}')