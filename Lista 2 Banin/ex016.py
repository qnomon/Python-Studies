lista = []

N = int(input('Digite o número de termos que deseja inserir: '))

for c in range(0, N):
    v = int(input('Digite um valor: '))
    while v in lista:
        print('O valor ja consta na lista. Adição cancelada.')
        v = int(input('Digite um valor: '))
    lista.append(v)
    print('Valor adicionado com sucesso.')
print(f'Os valores digitados foram{lista}')