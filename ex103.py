def ficha(jog='<desconhecido>', gols=0):
    if jog == '':
        jog = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {jog} marcou {gols} gol(s) no campeonato.'


a = str(input('Nome do Jogador:')).strip()
b = str(input('Número de Gols: ')).strip()
if b == '':
    b = 0
print(ficha(a,b))