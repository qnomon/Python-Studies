import random
A = []
B = []
nA = int(input('Digite quantos termos quer na lista A: '))
for c in range(0,nA):
    n = int(input('Digite um número: '))
    A.append(n)
nB = int(input('Digite quantos termos quer na lista B: '))
for c in range(0, nB):
    n = int(input('Digite um número: '))
    B.append(n)
print(f'A lista nA {A} possui {nA} elementos e a lista nB {B} possui {nB} elementos')
A.extend(B)
print(f'A lista resultante {A} possui {nA+nB} elementos')