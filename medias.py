#contador
cont = 0
tot = 0
print('Calcular medias')
print('Digite um numero negativo para encerrar')
#laco repeticao
while True:
    nota = float(input('Insira a nota: '))
    if nota < 0:
        break
    tot = tot + nota
    cont += 1
    calc = tot / cont
print(f'Media = {tot}/{cont}={calc}')