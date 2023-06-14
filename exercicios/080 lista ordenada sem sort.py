valores = []
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > max(valores):
        valores.append(v)
        print('Adicionando ao final da lista...')
    elif v < min(valores):
        valores.insert(0, v)
        print('Adicionando na posicao 0 da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos, v)
                print(f'Adicionado na posicao {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valores}')
