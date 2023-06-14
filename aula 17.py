#listas
#sao mutaveis, diferente das tuplas

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)

lanche[3] = 'picole'
print(lanche)

lanche.append('cookie')
print(lanche)

lanche.insert(0, 'hotdog')
print(lanche)

del lanche[4]
print(lanche)

lanche.pop(0) #sem especificar, apaga o ultimo elemento
print(lanche)

lanche.remove('cookie')
print(lanche)

#para nao dar erro se o cookie nao estiver na lista
if 'cookie' in lanche:
    lanche.remove('cookie')

valores = list(range(4, 11))
print(valores)

valores2 = [1,6,8,3,6,89,4,2,687]
valores2.sort()
print(valores2)
valores2.sort(reverse=True)
print(valores2)

print(len(valores2))

teste = []
teste.append(5)
teste.append(9)
teste.append(4)

for c, v in enumerate(teste):
    print(f'Na posicao {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista.')

'''
numeros = []
for val in enumerate(range(0, 5)):
    numeros.append(int(input('Insira um valor: ')))
for cont, val in enumerate(numeros):
    print(f'Na posicao {cont}, encontrei o valor {val}')
'''

a = [1,2,3,4]
b = a #b recebe a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[1] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a1 = [1,2,3,4]
b1 = a[:] #b recebe itens de a
b1[1] = 5
print(f'Lista A: {a1}')
print(f'Lista B: {b1}')

#existe diferenca entre receber a e receber todos os itens de a