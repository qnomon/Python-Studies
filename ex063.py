'''n = int(input('Digite um valor de elementos que deseja visualizar da sequência de Fibonacci: '))
a = 0
b = 0
c = 0
while n != 0:
    if a == 0:
        print(0, end=' -> ')
        print(1, end=' -> ') #A sequencia começa pelo 1 então soma-se com ele mesmo, logo imprime-se 1 e A soma-se a 1
        a = 1
    c = a + b               #C = Fibonacci Recebe a soma de A+B
    b = a                   #B recebe A por ser seu antecessor
    a = c                   #A Recebe C para que some-se com B que recebeu o antigo A.
    n -= 1
    print(c, end=' -> ')
print('Fim')'''
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=' -> ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')