listagem = ('Lápis', 0.5, 'Borracha', 1, 'Caderno', 18.50, 'Mochila', 95.90, 'Notebook', 2199, 'Mesa Digitalizadora', 459, 'Canetinhas', 25.50, 'Estojo', 5.50)
c = 0
nome = 'Kalunga'
print(f'{nome:.^60}')
print('-'*60)
while True:
    if c > 14:
        break
    print(f'{listagem[c]:.<50}R${listagem[c+1]:>8.2f}')
    c += 2
print('-'*60)