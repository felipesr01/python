import datetime

atual = datetime.date.today().year
num = 1
maior = 0
menor = 0
for c in range(1,8):
    perg = int(input(f'Em que ano a {num}ª pessoa nasceu? '))# pode trocar o num por c
    num += 1
    calc = (atual - perg)
    if calc >= 21:
        maior += 1
    elif calc < 21:
        menor += 1
print(f'Ao todo tem {menor} pessoas menores de idade\nE {maior} pessoas maiores de 21 anos!')