frase = str(input('Frase: ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('E um palindromo')
else:
    print('Nao palindromo')
