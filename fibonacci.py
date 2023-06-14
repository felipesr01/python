n1 = 0
n2 = 1
n3 = 0
while n3 <= 500:
    n3 = n1 + n2
    print(f'{n1}, {n2}, {n3}', end='')
    n1 = n2
    n2 = n3
