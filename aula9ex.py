'''
22 crie um programa que leia o nome completo de uma pessoa e mostre
nome com todas as letras maiusculas
nome com todas minusculas
quantas letras tem o nome sem considerar espacos
quantas letras tem o primeiro nome
23 ler um numero de 0 a 9999 e mostrar cada digito separado
24 ler nome de cidade e dizer se comeca ou nao com a palavra santo
25 ler nome de pessoa e dizer se tem silva no nome
26 ler frase e dizer
quantas vezes aparece a letra a
em que posicao aparece pela 1 vez
em que posicao aparece pela ultima vez
27 ler nome completo de uma pessoa e mostrar o primeiro e o ultimo nome separadamente
'''
#22
nome = str(input('Insira seu nome completo: ')).strip()
nome1 = nome.split()
nome2 = ''.join(nome1)

print(nome.upper())
print(nome.lower())
print(len(nome2))
print(len(nome1[0]))

#23
num = str(input('Insira um numero de 0 a 9999: '))
num0 = num[0:1]
num1 = num[1:2]
num2 = num[2:3]
num3 = num[3:4]
print(f'''
Unidade: {num3}
Dezena: {num2}
Centena: {num1}
Milhar: {num0}''')

#24
nome = str(input('Nome cidade: ')).lower().strip()
print('Comeca com Santo: ','santo' in nome[0:5])

#25
nome = str(input('Insira seu nome:')).lower().strip()
print('Tem Silva:','silva' in nome)

#26
frase = str(input('Insira uma frase: ')).lower()
frase1 = frase.strip()
print('a:',frase1.count('a'))
print('Primeiro a:',int(frase1.find('a'))+1)
print('Ultimo a:', frase1.rfind('a')+1)

#27
nome = str(input('Insira seu nome: '))
nome1 = nome.split()
print(f'Primeiro nome: {nome1[0]}')
print(f'Ultimo nome: {nome1[-1]}')
