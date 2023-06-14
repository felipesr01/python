def lin():
    print('-'*30)


#Programa principal
lin()
print('Curso em video')
lin()
print('Aprenda python')
lin()
print('Felipe Souza')
lin()


def tit(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


tit(' Aderbaldo ')

a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#Programa Principal
soma(4,5)
soma(a=4, b=5)
soma(b=5, a=4)


def contador(* num): #varios numeros
    tam = len(num)
    print(f'Recebi os numeros {num} e sao ao todo {tam}')


contador(2,1,7)
contador(8,2)
contador(4,4,7,6,2)


valores = [7,2,5,0,4]


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


dobra(valores)
print(valores)
