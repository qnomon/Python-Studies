from random import randint
print('Qual valor entre 0 e 10 o programa pensou? ')
r = randint(0,10)
q = 0
acerto = False
while not acerto:
    v = int(input('Qual é o seu palpite? '))
    q += 1
    if v > r :
        print('Menos... Tente novamente')
    if v < r:
        print('Mais... Tente novamente')
    if v == r:
        acerto = True
print(f'\033[34mParabéns\033[m, você acertou depois de \033[34m{q}\033[m tentativas')
