a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a+b > c and b+c > a and a+c > b:
    if a == b == c:
        print('Pode ser um triangulo Equilatero')
    elif a == b or a == c or b == c:
        print('Pode ser um triangulo Isosceles')
    elif a != b or a != c or b != c:
        print('Pode ser um triangulo Escaleno')
else:
    print('Nao pode ser um triangulo')