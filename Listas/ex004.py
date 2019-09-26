A = []
B = []
for c in range(0,10):
    n = int(input('Digite um número para a lista A: '))
    A.append(n)
for c in range(0,10):
    n = int(input('Digite um número para a lista B: '))
    B.append(n)

A.extend(B)
print(A)