import datetime
import random
import time
'''
nome = str(input('Qual o seu nome? ')).lower().strip()
if nome == 'felipe':
    print('Que nome bonito!!')
elif nome == 'pedro' or 'joao' or 'maria':
    print('Seu nome e bem popular no Brasil.')
else:
    print('Se nome e bem normal')
print(f'Tenha um bom dia, {nome.title()}!!')
36
37
38
39
40
41
42

#36
v = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o seu salario? R$'))
ta = int(input('Em quantos anos voce quer pagar? ')) #tempo em anos
tm = ta * 12 #tempo em meses
ex = s * 30/100 #calculo de 30% do salario
pm = v/tm
if pm > ex:
    print('Voce nao podera fazer esse emprestimo :(')
else:
    print('Seu emprestimo foi aprovado!')
    print(f'Voce pagara R${pm:.2f} por mes por {tm} meses')

#37
num = int(input('Insira um numero inteiro: '))
print(Escolha uma das opcoes para converter
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL) #adicionar tres apostrofos
op = int(input('Sua opcao: '))

if op == 1:
    print(f'{num} convertido para binario e {bin(num)[2:]}')
elif op == 2:
    print(f'{num} convertido para octal e {oct(num)[2:]}')
elif op == 3:
    print(f'{num} convertido para hexadecimal e {hex(num)[2:]}')
else:
    print('Insira um numero valido')

#38
n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
if n1 > n2:
    print(f'{n1} e maior que {n2}')
elif n2 > n1:
    print(f'{n2} e maior que {n1}')
elif n1 == n2:
    print('Os numeros sao iguais')
print('Fim do programa')

#39
d = int(input('Insira o dia do seu nascimento: '))
m = int(input('Insira o mes do deu nascimento: '))
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

#40
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print(f'Sua media foi {med}, esta reprovado!')
elif 5 <= med < 7:
    print(f'Sua media foi {med}, esta de recuperacao!')
elif med >= 7:
    print(f'Sua media foi {med}, esta aprovado!')

#41
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

#42
a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a+b > c and b+c > a and a+c > b:
    if a == b == c:
        print('Pode ser um triangulo Equilatero')
    elif a == b or a == c or b == c:
        print('Pode ser um triangulo Isosceles')
    elif a != b or a != c or b != c:
        print('Pode ser um triangulo Escaleno')
else:
    print('Nao pode ser um triangulo')

#43
peso = float(input('Insira seu peso: '))
alt = float(input('Insira sua altura: '))
imc = peso / (alt**2)
print(f'Seu IMC e de {imc}')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 < imc < 25:
    print('Peso ideal.')
elif 25 < imc < 30:
    print('Sobrepeso.')
elif 30 < imc < 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade morbida.')

#44
preco = float(input('Preco R$'))
print(FORMAS DE PAGAMENTO 
[ 1 ] a vista dinheiro
[ 2 ] a vista cartao
[ 3 ] 2x cartao
[ 4 ] 3x ou mais cartao) #adicionar 3 apostrofos
forma = int(input('Qual a opcao? ')) 
if forma == 1:
    preco = preco - preco*10/100
    print(f'Preco R${preco}')
elif forma == 2:
    preco = preco - preco*5/100
    print(f'Preco R${preco}')
elif forma == 3:
    print(f'Preco R${preco}')
    print(f'Sua compra sera parcelada em 2x de {preco/2}')
elif forma == 4:
    preco = preco + preco*20/100
    print(f'Preco R${preco}')
else:
    forma = 0
    print('\033[:31mInsira uma forma de pagamento valida\033[m')
'''
#45
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
user = str(input('Pedra, papel ou tesoura? ')).lower().strip()
print('-'*13)
print('Pe',end= '')
time.sleep(0.5)
print('dra')
time.sleep(1)
print('Papel')
time.sleep(1)
print('Te', end= '')
time.sleep(1)
print('soura')
print('-'*13)
print(f'Voce escolheu {user} e o programa escolheu {pc}')
if pc == user:
    print('empate!')
elif (user == 'pedra' and pc == 'tesoura') or (user == 'tesoura' and pc == 'papel') or (user == 'papel' and pc == 'pedra'):
    print('Venceu!')
else:
    print('Voce perdeu!')
