from random import randint
from time import sleep
lista = list()
def sorteia():
    print('Sorteando os 5 Valores da lista: ', end='')
    for c in range(0,5):
        a = randint(1,10)
        lista.append(a)
        print(a, end=' ')
        sleep(0.3)
    print('Pronto')


def somapar():
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia()
somapar()


