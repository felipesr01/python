def contador(i, f, p):
    if p < 0:
        p = abs(p)
    if p == 0:
        p = 1
    cont = i
    if i < f:
        while cont <= f:
            print(cont, end=' ')
            cont += p
    if i > f:
        while cont >= f:
            print(cont, end=' ')
            cont -= p


# Principal
contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
