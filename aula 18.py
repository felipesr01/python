'''
teste = []

teste.append('Felipe')
teste.append(20)
print(teste)
galera= []
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

print(galera)
print(galera[0])
print(galera[0][1])
print(galera[1][0])
print()
grupo = [['paulo', 82], ['miqueais', 10], ['andre', 50], ['gabriel', 26], ['reltomi', 28]]
for p in grupo:
    print(f'{p[0]} tem {p[1]} anos de idade')
'''

galera = []
dado = []
mai = 0
men = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade')
        mai += 1
    else:
        print(f'{p[0]} e menor de idade')
        men += 1

print(f'Maiores de idade: {mai}\nMenores de idade {men}')
