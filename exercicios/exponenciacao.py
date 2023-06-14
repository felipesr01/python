n1 = int(input('Base: '))
n2 = int(input('Expoente: '))
n3 = n1
for c in range(1, n2):
    n1 *= n3

print(n1)