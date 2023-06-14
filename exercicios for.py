'''
negs = 0
print('====Insira qualquer valor inteiro====')
for c in range(1,11):
    num = int(input(f'Insira o {c}ºvalor: '))
    if num < 0:
        negs += 1
print(f'Voce informou {negs} valores negativos')


frase = str(input('Insira uma frase: ')).strip().upper()
frasep = frase.split()
frasej = ''.join(frasep)
inverso = ''
for letra in range(len(frasej)-1,-1,-1):
    inverso += frasej[letra]
print(inverso, frasej)
if inverso == frasej:
    print("palindromo")
else:
    print('Nao palindromo')


print('=====TABUADA=====')
num = int(input('Insira um numero: '))
for c in range(1,11):
    print(f'{num} x {c} = {num*c}')

print('Os numeros pares de 1 a 100 sao')
for c in range(1,101):
    if c % 2 == 00:
        print(c)

for c in range(5, 101):
    if c % 7 == 0 and c % 5 != 0:
        print(c)

soma = 0
n = int(input('Insira o Numero: '))
for c in range(1, (n+1),1):
    print(c)
    soma += c
print(soma)

frase = str(input('Insira uma frase: '))
for letra in range(len(frase)-1, -1, -1):
    print(frase[letra],end='')

numeros = (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
pares = 0
impar = 0
for c in numeros:
    if c % 2 == 0:
        pares += 1
    else:
        impar += 1
print(f'Numeros impares: {impar}')
print(f'Numeros pares: {pares}')

frase = str(input('Escreva: ')).strip().lower()
digitos = 0
letras = 0
for c in frase:
    if c.isdigit():
        digitos += 1
    elif c.islower(): #ou usar isalpha
        letras += 1
print(f'{digitos} digitos e {letras} letras')


lista = []
for num in range(100,401):
    s = str(num)
    if (int(s[0]) % 2 ==0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        lista.append(s)
print(','.join(lista))


fat = 1
n = int(input('Insira o numero: '))
if n < 0:
    print("inserir numero positivo!")
elif n == 0:
    print(1)
else:
    for c in range(1,n+1):
        print(c, end=' ')
        fat = fat * c
    print('\n')
    print(fat)


nums = 0
nums2 = 0
for n in range(1,11):
    ins = int(input(f'Insira o {n}º numero: '))
    if 10 < ins < 20:
        nums += 1
    else:
        nums2 += 1
print(f'{nums} numeros estao entre 10 e 20')
print(f'{nums2} estao fora do intervalo')

#1
c = -1
while not -1 < c < 10:
    c = float(input('Insira a nota de 0 a 10: '))

#2
user = ''
senha = ''
while user == senha:
    user = str(input('Insira o nome de usuario: '))
    senha = str(input('Insira a senha: '))
    if user == senha:
        print('Usuario tem quer ser diferente da senha!')
    else:
        print('Conta criada com sucesso!')

#3
nome = str(input('Qual o seu nome? '))
idade = int(input('Qual sua idade? '))
sal = float(input('Qual o seu salario? '))
sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()
est = str(input('Qual seu estado civil? [S/C/V/D] ')).upper().strip()
while len(nome) < 3:
    nome = str(input('Seu nome tem que ter pelo menos 3 caracteres: '))
while idade < 0 or idade > 150:
    idade = int(input('sua idade nao pode ser negativa nem passar de 150: '))
while sal < 0:
    sal = float(input('Ninguem recebe salario menor que 0: '))
while sexo not in 'M,F':
    sexo = str(input('Escolha apenas as opcoes entre [M/F]: ')).upper().strip()
while est not in 'S,C,V,D':
    est = str(input('Escolha apenas as opcoes entre [S/C/V/D]: ')).upper().strip()

a = 80000
b = 200000
cresa = 5/100*a
cresb = 1.5/100*b
anos = 0
while a < b:
    a += cresa
    b += cresb
    anos += 1
    print(f'a{a}')
    print('\n')
    print(f'b{b}')
    print('\n')
    print(f'anos{anos}')


for c in range(1,21):
    print(c, end=' ')

#10
a = int(input('Insira o primeiro numero: '))
b = int(input('Insira o segundo numero: '))
while a < (b-1):
    a+= 1
    print(a)
'''
