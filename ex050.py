s = 0
count = 0
for c in range(0,6):
    n = int(input('Digite um valor: '))
    if n%2 == 0:
        s += n
        count += 1
print(f'O resultado da somatória de todos os {count} números pares é de {s}')
