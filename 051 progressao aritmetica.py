pt = int(input('Primeiro termo: '))
raz = int(input('Razao: '))
decimo = pt + (10-1) * raz
for c in range(pt, decimo + raz, raz):
    print(c, end=' ↦ ')
print('FIM')