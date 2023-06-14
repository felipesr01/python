import datetime

d = int(input('Insira o dia do seu nascimento: '))
m = int(input('Insira o mes do seu nascimento: '))
a = int(input('Insira o ano do seu nascimento: '))
ahj = datetime.date.today().year
idade = ahj - a
print(f'Voce tem {idade} anos')
if idade == 18:
    print('Esta na hora de voce se alistar')
elif idade < 18:
    print('Voce ainda vai se alistar')
    print(f'Ainda faltam {(idade-18)*-1} anos pra voce se alistar')
elif idade > 18:
    print('Voce ja se alistou')
    print(f'Fazem {idade-18} anos que voce se alistou')