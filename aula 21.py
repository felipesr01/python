def teste(b):
    # a = 8  # cria outra variavel "a", so que local
    global a  # torna a variavel local de "a" global
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
# print(f'B fora vale {b}')
# print(f'C fora vale {c}')
# nenhum funciona pq b e c so estao definidos no escopo local
print()


# RETURN
def somar(a=0, b=0, c=0):
    s = a + b + c
    # print(f'A soma vale {s}')  # se usar o retorno nao precisa escrver o print aq, so quando quiser mostrar
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'As somas valem respectivamente {r1}, {r2}, {r3}')

print()


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados sao: {f1}, {f2}, {f3}')
print()


def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('Insira um numero:'))
if par(n):
    print('E par')
else:
    print('Nao e par')
