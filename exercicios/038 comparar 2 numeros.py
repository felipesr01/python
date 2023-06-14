n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
if n1 > n2:
    print(f'{n1} e maior que {n2}')
elif n2 > n1:
    print(f'{n2} e maior que {n1}')
elif n1 == n2:
    print('Os numeros sao iguais')
print('Fim do programa')