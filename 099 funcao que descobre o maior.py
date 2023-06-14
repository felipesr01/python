def maior(* num):
    cont = maior = 0
    for n in num:
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'A lista é {num}. O maior é {maior}')


maior(2, 9, 5, 7, 8, 8, 4, 2)
maior(2, 6, 2, 6, 8, 9)
maior(3, 1, 5)
maior(2, 8)
maior(1)
maior()
