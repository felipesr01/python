peso = float(input('Insira seu peso: '))
alt = float(input('Insira sua altura: '))
imc = peso / (alt**2)
print(f'Seu IMC e de {imc}')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 < imc < 25:
    print('Peso ideal.')
elif 25 < imc < 30:
    print('Sobrepeso.')
elif 30 < imc < 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade morbida.')