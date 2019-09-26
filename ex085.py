num = [[], []]
pares = list()
impares = list()
for c in range (0,7):
    v = int(input(f'Digite o {c+1}° valor: '))
    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}\nOs valores ímpares digitados foram: {num[1]}')