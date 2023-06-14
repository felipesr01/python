def fat(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


print(fat(5))
