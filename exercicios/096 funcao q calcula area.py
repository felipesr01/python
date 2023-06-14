c = float(input('Insira o Comprimento: '))
l = float(input('Insira a Largura: '))


def area(c=0, l=0):
    return c * l


ar = area(c, l)
print(f'A area de um terreno {c} x {l} é de {ar}m2')
