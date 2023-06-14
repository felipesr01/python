num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    perg = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= perg <= 20:
        print(f'voce digitou o numero {num[perg]}')
    else:
        print('Invalido. ', end='')
        continue
    sn = str(input('Quer continuar? [S/N] ')).strip().lower()
    if sn == 'n':
        break
