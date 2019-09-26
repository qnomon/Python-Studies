import random
A = []
B = []
nA = int(input('Digite quantos termos quer na lista A: '))
for c in range(0,nA):
    n = int(input('Digite um número: '))
    while n in A:
        print('O valor ja consta na lista. Adição cancelada.')
        n = int(input('Digite um número: '))
    A.append(n)
nB = int(input('Digite quantos termos quer na lista B: '))
for c in range(0, nB):
    n = int(input('Digite um número: '))
    while n in B:
        print('O valor ja consta na lista. Adição cancelada.')
        n = int(input('Digite um número: '))
    B.append(n)
print(f'A lista nA {A} possui {nA} elementos e a lista nB {B} possui {nB} elementos')
for c in B:
    if c not in A:
        A.append(c)
print(f'A lista resultante {A} possui {len(A)} elementos')