ex = str(input('Escreva uma expressao: '))
lista = []
for simb in ex:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta invalida!')
