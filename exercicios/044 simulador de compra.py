preco = float(input('Preco R$'))
print('''FORMAS DE PAGAMENTO 
[ 1 ] a vista dinheiro
[ 2 ] a vista cartao
[ 3 ] 2x cartao
[ 4 ] 3x ou mais cartao)''')
forma = int(input('Qual a opcao? '))
if forma == 1:
    preco = preco - preco*10/100
    print(f'Preco R${preco}')
elif forma == 2:
    preco = preco - preco*5/100
    print(f'Preco R${preco}')
elif forma == 3:
    print(f'Preco R${preco}')
    print(f'Sua compra sera parcelada em 2x de {preco/2}')
elif forma == 4:
    preco = preco + preco*20/100
    print(f'Preco R${preco}')
else:
    forma = 0
    print('\033[:31mInsira uma forma de pagamento valida\033[m')