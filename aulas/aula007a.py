
'''
nome = input('Qual o seu nome? ')
print(f'Prazer em te conhecer {nome:=^20}!')
print(f'Prazer em te conhecer\n{nome:=<20}!')
print(f'Prazer em te conhecer {nome:20}!')

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1+n2
su = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
r = n1%n2
e = n1*n2

print(f'Soma {s}\nSubtracao {su}\nMultiplicacao {m}\nDivisao {d}\nDivisao Inteira {di}\nResto {r}\nPotencia {e}')
print('Esses sao os resultados', end=' ')
print('das operacoes')


DESAFIO
5 ler um numero e mostrar o sucessor e o antecessor
6 ler um numero e mostrar o dobro, o triplo e a raiz quadrada
7 ler as duas notas de um aluno e mostrar a media
8 ler valor em metros e mostrar em cm e mm
9 ler um numero inteiro e mostrar sua tabuada
10 ler quanto dinheiro ela tem na carteira e mostrar quantos dolares ela pode compra
11 ler largura e altura de uma parede em metros calcular a area e a quantidade de tinta, cada litro de tinta pinta 2m^2
12 ler o preco de um produto e aplicar desconto de 5%
13 ler salario de um funcionario e mostrar seu novo salario com 15% de aumento
'''
#5

nome = 'Sucessor e Antecessor'
print(f'Programa: \033[4:31:40m{nome:=^30}\033[m')

numero = int(input('Insira um numero: '))
ant = numero - 1
suc = numero + 1
print(f'Antecessor: \033[31m{ant}\033[m\nNumero: \033[34m{numero}\033[m\nSucessor: \033[32m{suc}\033[m')

#6

nome = 'D.T.RQ'
print(f'Programa \033[4:31:40m{nome:=^30}\033[m')
numero = int(input('Insira um numero: '))
d = numero * 2
t = numero * 3
r = numero ** (1/2)
print(f'Numero: \033[7m{numero}\033[m\nDobro: {d}\nTriplo: {t}\nRaiz Quadrada: {round(r, 2)}')85


#7

nome = 'Media'
print(f'Programa \033[4:31:40m{nome:=^30}\033[m')

n1 = float(input('Insira nota 1: '))
n2 = float(input('Insira nota 2: '))
media = (n1 + n2) / 2
print(media)

#8
nome = 'Conversao'
print(f'Programa \033[4:31:40m{nome:=^30}\033[m')
numero = float(input('Digite o Valor em Metros a ser Convertido: '))
km = numero / 1000
hm = numero / 100
dam = numero / 10
dm = numero * 10
cm = numero * 100
mm = numero * 1000
print(f'Km = {km}\nHm = {hm}\nDam = {dm}\nM = {numero}\nDm = {dm}\nCm = {cm}\nMM = {mm}')

#9
nome = 'Tabuada'
print(f'Progama {nome:=^30}')
numero = int(input('Insira o numero: '))
a = numero * 0
b = numero * 1
c = numero * 2
d = numero * 3
e = numero * 4
f = numero * 5
g = numero * 6
h = numero * 7
i = numero * 8
j = numero * 9
k = numero * 10
print(f'| {numero} x  0 = {a}')
print(f'| {numero} x  1 = {b}')
print(f'| {numero} x  2 = {c}')
print(f'| {numero} x  3 = {d}')
print(f'| {numero} x  4 = {e}')
print(f'| {numero} x  5 = {f}')
print(f'| {numero} x  6 = {g}')
print(f'| {numero} x  7 = {h}')
print(f'| {numero} x  8 = {i}')
print(f'| {numero} x  9 = {j}')
print(f'| {numero} x 10 = {k}')

#10
real = float(input('Insira seu valor em reais: R$ '))
dol = real / 5.20
eur = real / 5.53
yen = real * 26.14
print(f'R${real} sao U${round(dol, 2)} em 2023')
print(f'R${real} sao €{round(eur, 2)} em 2023')
print(f'R${real} sao ¥{round(yen, 2)} em 2023')

#11
lar = float(input('Insira a largura da parede: '))
alt = float(input('Insira a altura da parede: '))
ar = lar * alt
tinta = ar / 2
print(f'A area da parede é de {ar}m²\nSerao precisos {tinta} litros de tinta')

#12
v1 = float(input('Insira o valor do produto: R$'))
v2 = v1 * 0.05 #ou v1 * 5 / 100
v3 = v1 - v2 #ou v1 - (v1 * 5 / 100)
print(f'O valor com desconto de 5% e {v3}')

#13
si = float(input('Insira o salario: R$'))
au = si * 0.15
sf = si + au
print(f'Seu salario agora e de {sf} reais')

#14
c = float(input('Informe a temperatura em ºC: '))
far = (c * 9/5) + 32
print(f'{c}ºC equivalem a {far}ºFahrenheit')

#15
dia = int(input('Quantos dias usados? '))
km = float(input('Quantos Km rodados? '))
ckm = 0.15 * km
cdia = 60 * dia
print(f'O valor total a pagar e de R${cdia + ckm}')
