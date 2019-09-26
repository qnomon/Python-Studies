n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
c = 0
while c != 10:
    pa = n + (r*c)
    print(pa, end=' → ')
    c += 1
print('Fim')

