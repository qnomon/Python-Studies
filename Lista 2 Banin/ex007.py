min = int(input('Digite o valor mínimo: '))
max = int(input('Digite o valor máximo: '))
placeholder = 0
A = list()
N = int(input('Digite a quantidade de valores que deseja inserir: '))
if min > max:
    placeholder = max
    max = min
    min = placeholder

for x in range(0,N):
    num = int(input('Digite um valor: '))
    if num >= min and num <= max:
        A.append(num)
print(f'A lista gerada entre os intervalos é {A} e contém {len(A)} elementos')


