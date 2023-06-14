def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos o voto sera NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto sera FACULTATIVO'
    elif 18 <= idade < 70:
        return f'Com {idade} anos o voto sera OBRIGATORIO'


ano = int(input('Em que ano voce nasceu? '))
print(voto(ano))
