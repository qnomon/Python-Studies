v = 2
validador = contador = 0
lista = []
N = int(input('Quantos números primos deseja mostrar? '))
while contador != N:
    for c in range(1, v):
        if v % c == 0:
            validador += 1
    if validador == 1:
        lista.append(v)
        contador +=1
    validador = 0
    v +=1
for i,v in enumerate(lista):
    print(f'Primo {i+1} = {v}')