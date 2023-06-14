real = float(input('Insira seu valor em reais: R$ '))
dol = real / 5.20
eur = real / 5.53
yen = real * 26.14
print(f'R${real} sao U${round(dol, 2)} em 2023')
print(f'R${real} sao €{round(eur, 2)} em 2023')
print(f'R${real} sao ¥{round(yen, 2)} em 2023')