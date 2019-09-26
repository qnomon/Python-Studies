import random

N = 0
lista = []
lista2 = []
while N < 10:
    N = int(input('Digite um número maior que 10: '))
for c in range(0, N):
    a = random.randint(0,100)
    lista.append(a)
print(f'A lista gerada foi {lista}')
for c,v in enumerate(lista):
    if c == 0 or v > lista2[len(lista2) - 1]:
        lista2.append(v)
    else:
        pos = 0
        while pos < len(lista2):
            if v <= lista2[pos]:
                lista2.insert(pos, v)
                break
            pos += 1
print(f'A lista em ordem é {lista2}')
