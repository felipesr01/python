grupo = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).lower().strip()[0]
    while pessoa['sexo'] not in 'mf':
        pessoa['sexo'] = str(input('[M/F]: ')).lower().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    op = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    while op not in 'sn':
        op = str(input('[S/N]: ')).lower().strip()[0]
    if op == 'n':
        break
print('-='*30)
print(f'Pessoas cadastradas: {len(grupo)}')
media = soma / len(grupo)
print(f'Media idade: {media:5.2f}')

print(f'Mulheres cadastradas: ')
for p in grupo:
    if p['sexo'] == 'f':
        print(f'{p["nome"]}', end='...')
print()
print(f'Pessoas acima da media: ')
for p in grupo:
    if p['idade'] > media:
        print(f'{p["nome"]}', end='...')
