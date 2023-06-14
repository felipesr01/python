dados = []
boletim = []
while True:
    nome = str(input('Nome: ')).strip().title()
    dados.append(nome)
    n1 = float(input('Nota 1: '))
    while n1 > 10:
        n1 = float(input('Insira uma nota de 0 a 10: '))
    dados.append(n1)
    n2 = float(input('Nota 2: '))
    while n2 > 10:
        n2 = float(input('Insira uma nota de 0 a 10: '))
    dados.append(n2)
    media = (n1 + n2) / 2
    dados.append(media)
    boletim.append(dados[:])
    dados.clear()

    op = str(input('Quer continuar? [S/N] ')).strip().lower()
    while op not in 'sn':
        op = str(input('[S/N]: '))
    if op == 'n':
        break
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8} ')
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
print(len(boletim))
while True:
    perg = int(input('Quer ver as notas de qual aluno? (negativo para encerrar) '))
    print(f'Nome: {boletim[perg][0]}\nNota 1: {boletim[perg][1]}\nNota 2: {boletim[perg][2]}\nMedia: {boletim[perg][3]}')
    if perg < 0:
        break
print('Volte sempre!')
