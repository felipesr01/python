import random
import time
'''
for c in range(1,10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1

n = 1
imp = 0
par = 0
while n != 0:
    n = int(input('Insira uma numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            imp += 1
print('FIM')
print(f'Impares {imp}')
print(f'Pares {par}')

#exercicios

#57
perg = str(input('Insira seu sexo [M/F]: ')).upper().strip()[0]
while perg not in 'MF':
    perg = str(input('Insira apenas M ou F: ')).upper().strip()[0]
if perg == 'F':
    print('Seu sexo e feminino!')
else:
    print('Seu sexo e masculino')
'''
#58
comp = random.randint(0,10)
tent = 1
print('Pensei em um numero de 0 a 10')
time.sleep(1)
print('Consegue advinhar?')
#print(comp)
user = int(input('Seu chute: '))
while user != comp:
    if user > comp:
        tent += 1
        user = int(input('Chute mais baixo! '))
    elif user < comp:
        user = int(input('Chute mais alto! '))
        tent += 1
if user == comp:
    print(f'Voce acertou com {tent} tentativas')
'''
#59

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
sair = 4
while sair != 5:
    print([1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Numeros
[5] Sair\n)
    op = int(input('O que deseja fazer? '))
    if op == 1:
        print(f'A soma de {n1} + {n2} = {n1+n2}')
    elif op == 2:
        print(f'A multiplicacao de {n1} x {n2} = {n1*n2}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} maior que {n2}')
        elif n2 > n1:
            print(f'{n2} maior que {n1}')
        elif n1 == n2:
            print('Numeros iguais')
    elif op == 4:
        n1 = int(input('Insira o novo primeiro valor: '))
        n2 = int(input('Insira o novo segundo valor: '))
    elif op == 5:
        print('Saindo')
        sair += 1

#60

n = int(input('Insira o Numero: '))
cont = n
fat = 1
print(f'Calculando {n}!')
while cont > 0:
    print(f'{cont}', end=' ')
    print('x' if cont > 1 else '=', end=' ')
    fat *= cont
    cont -= 1
print(fat)

#60 for
n = int(input('Insira um numero: '))
f = 1
for c in range(n,0,-1):
    f *= c
    print(c)
print(f)

#61
prim = int(input('Primeiro termo: '))
raz = int(input('Razao: '))
termo = prim
cont = 1
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += raz
    cont += 1
print('Fim')

#62
prim = int(input('Primeiro termo: '))
raz = int(input('Razao: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += raz
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais? '))
print('Fim')
print(f'Foram mostrados {total} termos')

#63
n = int(input('Quantos termos?'))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} -> {t2}', end='')
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> fim')

#64
n = int(input('Digire um numero [999 para parar]: '))
cont = 0
soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digire um numero [999 para parar]: ')) #se colocar o n como a ultima linha, o 999 nao vai ser contado
print(f'Voce digitou {cont} numeros e a soma foi de {soma}')

#65
op = 's'
cont = 0
soma = 0
maior = 0
menor = 0
#pra nao colocar varias variaveis e so igualar elas na mesma linha ( cont = soma = maior = menor = 0)
while op in 's':
    n = int(input('Digite um numero: '))
    op = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
med = soma/cont
print(f'Voce digitou {cont} numeros')
print(f'A media entre eles foi de {med}')
print(f'O maior entre eles foi o {maior}')
print(f'O menor entre eles foi o {menor}')
'''