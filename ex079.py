lista = list()
cont = ''
print('=-'*30)
while True:
    v = int(input('Digite um valor: '))
    if v in lista:
        print('O valor ja consta na lista. Adição cancelada.')
    else:
        lista.append(v)
        print('Valor adicionado com sucesso.')
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont == 'N' :
        break
lista.sort()
print('=-'*30)
print(f'Os valores digitados foram{lista}')
