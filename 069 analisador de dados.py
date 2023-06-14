print('Cadastre uma pessoa')
i18 = 0
h = 0
m20 = 0
while True:
    idade = ' '
    while idade not in range(1, 150):
        idade = int(input('Idade: '))
    sex = ' '
    while sex not in 'mf':
        sex = str(input('Sexo [M/F]: ')).strip().lower()[0]
    if idade >= 18:
        i18 += 1
    elif sex == 'm':
        h += 1
    elif sex == 'f' and idade < 20:
        m20 += 1
    perg = ' '
    while perg not in 'sn':
        perg = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if perg == 'n':
        break
print(f'Pessoas com mais de 18 anos: {i18}')
print(f'Homens cadastrados: {h}')
print(f'Mulheres com menos de 20 anos: {m20}')
