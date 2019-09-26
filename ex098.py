from time import sleep

def contagem(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}')

    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='')
            cont += c
            sleep(0.3)
        print('Fim')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='')
            cont -= c
            sleep(0.3)
        print('Fim')


contagem(1,10,1)
contagem(10,0,2)
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem(a,b,c)
