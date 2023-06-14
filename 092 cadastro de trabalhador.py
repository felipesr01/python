from datetime import date
datual = date.today()
aatual = datual.year
pessoa = {}

pessoa['Nome'] = str(input('Nome: '))
pessoa['Ano'] = int(input('Ano de Nascimento: '))
pessoa['Idade'] = aatual - pessoa['Ano']
pessoa['CTPS'] = int(input('CTPS (Nao tem: 0): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano Contratacao'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = float(input('Salario: R$'))
    pessoa['Idadecomeco'] = pessoa['Ano Contratacao'] - pessoa['Ano']
    pessoa['Aposentadoria'] = pessoa['Idadecomeco'] + 35
    del pessoa['Idadecomeco']
    del pessoa['Ano']
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
else:
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
