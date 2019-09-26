n = float(input('Digite um número: '))
r = float(input('Digite a razão: '))
t = int(input('Quantos termos quer exibir? '))
c = tot = 0
print(f'Os {t} primeiros termos da PG com primeiro termo {n} e razão {r}')

while c < t:
    tot += n
    print(n, end=' → ')
    n *= r
    c += 1
print('Fim')
print(f'A soma de todos os termos é igual a {tot}')
