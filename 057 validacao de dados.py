perg = str(input('Insira seu sexo [M/F]: ')).upper().strip()[0]
while perg not in 'MF':
    perg = str(input('Insira apenas M ou F: ')).upper().strip()[0]
if perg == 'F':
    print('Seu sexo é feminino!')
else:
    print('Seu sexo é masculino!')
