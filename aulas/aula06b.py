'''
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2

print(f'A soma entre {n1} e {n2} é {s}')
'''

algo = input('Digite algo: ')
print('O tipo primitivo desse valor e: ', type(algo))

print('e numerico ou alfabetico? ', algo.isalnum())
print('e alfabetico? ', algo.isalpha())
print('e ascii? ', algo.isascii())
print('e digito? ', algo.isdigit())
print('e minusculo? ', algo.islower())
print('e maiusculo? ', algo.isupper())
print('e identificador? ', algo.isidentifier())
print('e decimal? ', algo.isdecimal())
print('e numerico? ', algo.isnumeric())
print('e sprintavel? ', algo.isprintable())
print('e titulo? ', algo.istitle())
print('So tem espacos? ', algo.isspace())