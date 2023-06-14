import random
import datetime

'''
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('Fim')

ou

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('Fim')

nome = str(input('Qual o seu nome? ')).lower().strip()
if nome == 'felipe':
    print(f'Ola {nome.title()}!!')
    print('Que nome lindo em')
else:
    print(f'Ola {nome}!!')

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
print(f'Sua media è {m}')
if m >= 7:
    print('Otimo aluno, parabens!')
else:
    print('Precisa estudar mais')

28 computador pensa num numero de 0 a 5 e pede pro usuario descobrir depois mostrar na tela se ele venceu ou perdeu
29 ler velocidade de um carro se ele ultrapassar 80km mostre uma mensagem dizendo que ele foi multado e a multa vai custar 7 reais por cada km acima do limite
30 ler num inteiro e mostrar na tela se e par ou impar
31 ler distancia de uma viagem em km, calcular preco, cobrar 0,50 por km p viagens de ate 200 km, 0,45 para mais longas
32 ler um ano e dizer se e bisexto
33 ler 3 num e dizer qual o maior e o menor
34 ler salario e calcular aumento, para salarios maior q 1250 aumento de 10%, inferiores ou iguais, 15%
35 ler o comprimento de 3 retas e dizer se podem ou nao formar um triangulo

#28
n = random.randint(0, 5)
print(n)
nu = int(input('Adivinhe o numero de 0 a 5: '))
if nu != n:
    print('Errou!')
    print(f'Eu pensei em {n} nao em {nu}')
else:
    print('Acertou!')

#29
v = float(input('Insira velocidade: '))
ex = v - 80
m = 7 * ex
if v > 80.0:
    print('Multado!')
    print(f'Estava a {ex}km/h acima do limite, pagara R${m}')
else:
    print('Ta suave fi')

#30
n = int(input('Insira um numero: '))
div = n%2
if div == 0:
    print('Numero Par')
else:
    print('Numero Impar')

#31
v = float(input('Insira a distancia da viagem: '))
x = 0.50 * v
y = 0.45 * v
if v <= 200.0:
    print(f'Valor da viagem e R${x}')
else:
    print(f'Valor da viagem e R${y}')

#32
ano = int(input('Insira um ano. Ou digite 0 para ser ano atual: '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print(f'{ano} Ano bissexto')
else:
    print(f'{ano} Ano nao bissexto')

#33
n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o ultimo numero: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} e o maior')
if n2 > n1 and n2 > n3:
    print(f'{n2} e o maior')
if n3 > n1 and n3 > n2:
    print(f'{n3} e o maior')

#34
s = float(input('Insira seu salario: R$'))
s10 = s * 10/100
s15 = s * 15/100

if s > 1250.0:
    print(f'Seu salario vai de R${s} para R${s+s10}')
else:
    print(f'Seu salario vai de R${s} para R${s+s15}')
'''
#35
a = float(input('Insira o comprimento do primeiro lado: '))
b = float(input('Insira o comprimento do segundo lado: '))
c = float(input('Insira o comprimento do ultimo lado: '))

if a+b > c and b+c > a and a+c > b:
    print('Pode ser um triangulo')
else:
    print('Nao pode ser um triangulo')
'''
# 33 mais simples
a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor e {menor}')
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor e {maior}')
'''