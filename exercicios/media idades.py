cont = 0
soma = 0
print('Media do grupo!')
print('Digite um numero negativo para parar!')
while True:
    idade = int(input('Insira sua idade: '))
    if idade < 0:
        break
    soma = soma + idade
    cont += 1
    med = soma / cont
print(f'A media da idade do grupo e de {med} o grupo é', end=' ')
if med <= 25:
    print('jovem.')
elif 26 < med <= 60:
    print('adulto.')
else:
    print('idoso.')