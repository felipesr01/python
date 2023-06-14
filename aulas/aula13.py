import time
import datetime
import emoji

'''
for c in range(0,7):
    print(c)

for d in range(6,-1,-1):
    print(d)
print('Fim')


#46
for c in range(10,-1, -1):
    print(c)
    time.sleep(1)
print(emoji.emojize( ':fireworks: Feliz ano novo!! :fireworks:'))

#47
com = int(input('Inicio: '))
fim = int(input('Fim: '))
var = int(input('Pulando de: '))
for c in range((com-1), (fim+2), var):
    print(c)

#48
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'A soma de todos os {cont} valores e {s}')

#49
n = int(input('Insira um numero: '))
for c in range(0, 11):
    print(f'{n} x {c} = {n*c}')

#50
s = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'{c} Valor: '))
    if num % 2 == 0:
        s += c
        cont += 1
print(s)
print(cont)

#51
pt = int(input('Primeiro termo: '))
raz = int(input('Razao: '))
decimo = pt + (10-1) * raz
for c in range(pt, decimo + raz, raz):
    print(c, end=' ↦ ')
print('FIM')

#52
num = int(input('Numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        tot += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n')
print(f'\033[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print("E primo")
else:
    print('Nao e primo')

#53
frase = str(input('Frase: ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('E um palindromo')
else:
    print('Nao palindromo')

#refazendo
#51
prim = int(input('Insira o primero termo: '))
raz = int(input('Insira a razao: '))
nesimo = prim + (11-1) * raz
for c in range(prim,nesimo,raz):
    print(c, end=' > ')
print('Fim')

#52
n = int(input('Digite um numero: '))
vezes = 0
for c in range(1, n+1):
    if n % c == 0:
        vezes += 1
        print('\033[35m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n')
print(f'\033[mOnumero {n} foi divisivel {vezes} vezes')
if vezes == 2:
    print('Numero primo!')
else:
    print('Nao e primo.')

#53
palavra = str(input('Insira uma frase: ')).upper().strip()
frases = palavra.split()
frasej = ''.join(frases)
inverso = ''
for letra in range(len(frasej)-1,-1,-1):
    inverso += frasej[letra]
print(frasej, inverso)
if frasej == inverso:
    print('E um palindromo')
else:
    print('Nao palindromo')

#54
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
print(f'Ao todo tem {menor} pessoas menor de idade\nE {maior} pessoas maiores de idade!')

#55
for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor} Kg')



somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = ''
contmulher = 0
for p in range(1,5):
    print(f'---- {p}ª pessoa ----')
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    #analisar homem mais velho
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulher += 1

mediaidade = somaidade/4
print(f'A media de idade do grupo e de {mediaidade} anos')
print(f'O homem mais velho se chama {nomevelho} e ele tem {maiorhomem} anos')
print(f'Existem {contmulher} mulheres com menos de 20 anos')
'''
