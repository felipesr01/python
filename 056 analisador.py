somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = ''
contmulher = 0
for p in range(1,5):
    print(f'---- {p}ª pessoa ----')
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    #analisar homem mais velho
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulher += 1

mediaidade = somaidade/4
print(f'A media de idade do grupo e de {mediaidade} anos')
print(f'O homem mais velho se chama {nomevelho} e ele tem {maiorhomem} anos')
print(f'Existem {contmulher} mulheres com menos de 20 anos')