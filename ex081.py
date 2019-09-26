lista = list()
while True:
    v = int(input('Digite um valor: '))
    c = str(input('Deseja Continuar?[S/N]: ')).strip().upper()
    lista.append(v)
    while c not in 'SN':
        c = str(input('Dseja Continuar? [S/N]: ')).strip().upper()
    if c == 'N':
        break
lista.sort(reverse=True)
print(f'Foram inseridos {len(lista)} valores na lista\nOs valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi inserido na lista')
else:
    print('O valor 5 não foi inserido na lista')
