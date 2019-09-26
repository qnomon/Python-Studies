min = int(input('Digite o valor mínimo: '))
max = int(input('Digite o valor máximo: '))
placeholder = 0
A = list()
if min > max:
    placeholder = max
    max = min
    min = placeholder
for c in range(min, max+1):
    if c % 7 == 0:
        A.append(c)
print(f'Os números divisiveis por 7 entre {min} e {max} são: {A}')