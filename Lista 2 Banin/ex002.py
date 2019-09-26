lista = list()

for x in range (0,10):
    a = int(input('Digite um valor: '))
    lista.append(a)
lista.reverse()
for x in lista:
    print(x)