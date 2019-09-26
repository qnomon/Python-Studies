'''from math import factorial
a = int(input('Digite um valor para calcular o fatorial: '))
b = a
c = factorial(a)
while b >= 2:
    print(f'{a} x {b-1}', end=' > ')
    b -= 1
print(c)'''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
    print(f)