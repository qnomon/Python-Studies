lista = []
N = int(input('Digite o número de elementos: '))
c = 0

for x in range(0, N):
    A = int(input('Digite um valor: '))
    lista.append(A)

for x in lista:
    for i, v in enumerate(lista):
        if x == v:
            c += 1
            if c > 1:
                del (lista[i])
    c = 0

print(lista)

