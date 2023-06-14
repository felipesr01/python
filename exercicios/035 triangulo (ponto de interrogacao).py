a = float(input('Insira o comprimento do primeiro lado: '))
b = float(input('Insira o comprimento do segundo lado: '))
c = float(input('Insira o comprimento do ultimo lado: '))

if a+b > c and b+c > a and a+c > b:
    print('Pode ser um triangulo')
else:
    print('Nao pode ser um triangulo')