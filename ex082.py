lista = list()
impar = list()
par = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    c = str(input('Deseja Continuar?[S/N]: ')).strip().upper()
    while c not in 'SN':
        c = str(input('Deseja Continuar?[S/N]: ')).strip().upper()
    if c == 'N':
        break
lista.sort()
for cont, valor in enumerate (lista) :
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('=-'*30)
print(f'Todos os valores digitados: {lista}')
print(f'Apenas os valores pares: {par}')
print(f'Apenas os valores ímpares: {impar}')
