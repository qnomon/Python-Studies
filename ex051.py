n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
print(f'Os 10 primeiros termos da PA com primeiro termo {n} e razão {r}')
for c in range(n, n + r * 10, r):
    print(c, end=' → ')
print('Fim')
