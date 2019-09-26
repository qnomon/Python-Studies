n = int(input('Quantos termos você quer mostrar? '))
Prim = int(input('Digite o valor de Prim: '))
t1 = 0
t2 = 1
cont = 3
while cont <= n+2:
    t3 = t1 + t2
    if t3 > Prim:
        print(f'{t3}', end=' -> ')
        cont += 1
    t1 = t2
    t2 = t3
print('Fim')