A = []
B = []
R = []
c = 0
nA = int(input('Digite o tamanho da lista A: '))
while c < nA:
    valor = int(input('Digite um valor para inserir na lista A: '))
    while valor in A:
        valor = int(input('Digite um valor NÃO REPETIDO para inserir na lista A: '))
    A.append(valor)
    c +=1
c = 0
nB = int(input('Digite o tamanho da lista B: '))
while c < nB:
    valor = int(input('Digite um valor para inserir na lista B: '))
    while valor in B:
        valor = int(input('Digite um valor NÃO REPETIDO para inserir na lista B: '))
    B.append(valor)
    c +=1
for c in A:
    if c in A and c in B:
        R.append(c)
R.sort()
print(f'A lista A tem a quantidade de {nA} elementos e possui os elementos {A}')
print(f'A lista B tem a quantidade de {nB} elementos e possui os elementos {B}')
print(f'A lista R tem a quantidade de {len(R)} elementos e possui os elementos {R}')
