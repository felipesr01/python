def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
                print(f'{f}')
        f *= c
    return f


print(fatorial(5, False))
