            #Tuplas
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(lanche)
print(lanche[1])
print(len(lanche))


for cont in range(0, len(lanche)):
    print(f'Eu comi {lanche[cont]} na posicao {cont}')


for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posicao {pos}')
print('Comi pra caramba')

print((sorted(lanche))) #bota em ordem alfabetica

a = (1, 2, 3, 4, 5)
b = (2, 1, 6, 3, 6, 1, 3)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(2))
print(c.index(6))