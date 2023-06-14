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