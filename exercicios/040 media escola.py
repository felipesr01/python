n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print(f'Sua media foi {med}, esta reprovado!')
elif 5 <= med < 7:
    print(f'Sua media foi {med}, esta de recuperacao!')
elif med >= 7:
    print(f'Sua media foi {med}, esta aprovado!')