from random import randint
from time import sleep
lista= list()
jogos = list()
e = int(input('Quantos jogos você quer fazer?: '))
for cont in range(0,e):
    for c in range (0,6):
        r = (randint(1,60))
        if r in lista:
            r = randint(1,60)
        lista.append(r)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('=-'*30)
for i, l in enumerate (jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-'*10,'Boa sorte', '-='*10)