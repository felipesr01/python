print('Loja!')
total = 0
prodmil = 0
nmenor = ' '
vmenor = 0
cont = 0
while True:
    nome = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    cont += 1
    while preco < 1:
        preco = float(input('Insira um preco valido: '))
    total = total + preco
    if preco >= 1000:
        prodmil += 1
#analisando menor velor
    if cont == 1 or preco < vmenor:
        vmenor = preco
        nmenor = nome

    perg = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    while perg not in 'sn':
        perg = str(input('Escolha entre [S/N]: '))
    if perg == 'n':
        break
print('Fim...')
print(f'O total da compra foi R${total}')
print(f'{prodmil} produtos custaram mais de R$1000')
print(f'O produto mais barato foi {nmenor} e custou R${vmenor}')