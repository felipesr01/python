frase = str(input('Insira uma frase: ')).lower()
frase1 = frase.strip()
print('a:', frase1.count('a'))
print('Primeiro a:', int(frase1.find('a'))+1)
print('Ultimo a:', frase1.rfind('a')+1)