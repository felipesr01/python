nome = str(input('Insira seu nome completo: ')).strip()
nome1 = nome.split()
nome2 = ''.join(nome1)

print(nome.upper())
print(nome.lower())
print(len(nome2))
print(len(nome1[0]))