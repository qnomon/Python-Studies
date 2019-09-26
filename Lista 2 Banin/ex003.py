lista = list()

num = -1

while num < 0 or num > 50:
    num = int(input('Digite um número entre 0 e 50: '))

for x in range (0,num):
    a = int(input('Digite um valor: '))
    lista.append(a)

for x in lista:
    print(x)