aluno = {}

aluno['Nome'] = str(input('Nome do aluno: ')).title()
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
while aluno['Media'] > 10:
    aluno['Media'] = float(input('1 a 10: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] <7:
    aluno['Situação'] = 'Recuperacao'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é {v}')
