from random import randint
N = int(input('Digite quantos números deseja: '))
lista = []
for x in range (0,N):
    a = randint(0,1000)
    lista.append(a)
print(lista)

X = int(input('Qual número saber se está na lista? '))

if X in lista:
    for x, v in enumerate (lista):
        if v == X:
            del(lista[x])
else:
    print(f'O número {X}, não esta na lista')

print(f'Nova lista {lista}')
