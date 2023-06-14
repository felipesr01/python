pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {(pessoas["nome"])} tem {(pessoas["idade"])} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
#dicionario dentro de uma lista

brasil = []
estado1 = {'uf': 'Ceara', 'sigla': 'CE'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])
print()

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #nao funciona o [:]
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()