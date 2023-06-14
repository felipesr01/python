times = ('fluminense', 'botafogo', 'fortaleza', 'palmeiras', 'vasco da gama', 'internacional', 'bragantino', 'flamengo',
         'sao paulo', 'goias', 'athletico-pr', 'cruzeiro', 'gremio', 'corinthians', 'cuiaba', 'athletico-mg', 'santos',
         'bahia', 'coritiba', 'america-mg')
print(f'Lista de times {times}')
print('-=' * 15)
print(f'5 Primeiros Colocados: {times[0:5]}')
print('-=' * 15)
print(f'4 Ultimos Colocados: {times[-4:]}')
print('-=' * 15)
print(f'Ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'Fortaleza esta na {times.index("fortaleza")+1}a posicao')