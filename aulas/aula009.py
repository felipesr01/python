
frase = 'Curso em video Python'
frase2 = '   Aprenda Python  '
dividido = frase.split()
print(frase)
print(frase[9:21])
print(frase[9:20])
print(frase[:21])
print(frase[9:])
print(frase[:21:2])
#analise
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
#transformacao
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase2)
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
#divisao
print(frase.split())
print(dividido)
print(dividido[0])
print('-'.join(frase))
print('-'.join(dividido))

print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''')