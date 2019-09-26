min = int(input('Digite um valor mínimo de alcance: '))
max = int(input('Digite um valor máximo de alcance: '))
c = min
tot = 0
while c <= max:
    if c%5 == 0 and c != 0:
        print(c, end=' -> ')
        tot += 1
    c += 1
print('Fim')
print(f'O processo foi finalizado com {tot} valores divisiveis por 5')