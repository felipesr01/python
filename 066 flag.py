quant = 0
n = s = 0
while True:
    n = int(input('Numero: '))
    if n == 0:
        break
    s += n
    quant += 1
print(f'Digitou {quant} numeros, a soma vale {s}')