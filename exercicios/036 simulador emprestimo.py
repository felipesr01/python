v = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o seu salario? R$'))
ta = int(input('Em quantos anos voce quer pagar? '))
tm = ta * 12 #tempo em meses
ex = s * 30/100 #calculo de 30% do salario
pm = v/tm
if pm > ex:
    print('Voce nao podera fazer esse emprestimo :(')
else:
    print('Seu emprestimo foi aprovado!')
    print(f'Voce pagara R${pm:.2f} por mes por {tm} meses')