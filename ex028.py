from random import randint
v = int(input('Qual valor entre 0 e 5 o programa pensou? '))
r = randint(0,5)
if r == v:
    print('Parabéns, você acertou')
else:
    print(f'O programa pensou no valor {r} e venceu.')