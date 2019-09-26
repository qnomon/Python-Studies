jogador = {}
gols =[]
tot = 0
jogador['nome'] = str(input('Nome: '))
jogos = int(input('Quantos Jogos: '))
for c in range (0, jogos):
    golp = int(input(f'Quantos gols no jogo {c+1}: '))
    gols.append(golp)
    tot += golp
jogador['gols'] = gols
jogador['total'] = tot
print('=-'*30)
print(jogador.items())
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} jogos.')
for i, v in enumerate(jogador["gols"]):
    print(f'Na partida {i+1}, Marcou {v} Gols.')