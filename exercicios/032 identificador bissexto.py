import datetime
ano = int(input('Insira um ano. Ou digite 0 para ser ano atual: '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print(f'{ano} Ano bissexto')
else:
    print(f'{ano} Ano nao bissexto')