s = float(input('Insira seu salario: R$'))
s10 = s * 10/100
s15 = s * 15/100

if s > 1250.0:
    print(f'Seu salario vai de R${s} para R${s+s10}')
else:
    print(f'Seu salario vai de R${s} para R${s+s15}')