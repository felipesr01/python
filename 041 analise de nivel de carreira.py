import datetime

dd = int(input('Dia nascimento: '))
mm = int(input('Mes nascimento: '))
aa = int(input('Ano nascimento: '))
ahj = datetime.date.today().year
idade = ahj - aa
if idade <= 9:
    print(f'{idade} Mirim')
elif 9 < idade <= 14:
    print(f'{idade} Infantil')
elif 14 < idade <= 19:
    print(f'{idade} Junior')
elif idade <= 25:
    print(f'{idade} Senior')
elif idade > 25:
    print(f'{idade} Master')