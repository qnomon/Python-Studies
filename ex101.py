def voto():
    from datetime import date
    idade = date.today().year - nasc
    if idade >= 65 or idade >= 16 <18:
        return f'Com {idade} anos o voto é OPCIONAL'
    if idade >= 18:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'
    if idade < 16:
        return f'Com {idade} anos NÃO VOTA'


nasc = int(input('Digite o ano do nascimento: '))
print(voto())