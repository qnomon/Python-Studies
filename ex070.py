t = mil = p = c = 0
barato = ''
print('-'*20)
print('Loja TecShow')
print('-'*20)
while True:
    c += 1
    prod = str(input('Digite o nome do produto: '))
    valor = float(input(('Digite o valor do produto: R$')))
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    p += valor
    while not cont in 'SsnN':
        cont = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if c == 1:
        m = valor
    if valor >= 1000:
        mil += 1
    if m > valor:
        m = valor
        barato = prod
    if cont == 'N':
        break
print(f'O total da compra é de R${p:.2f}\n{mil} Produtos custam mais de R$1000.00\nO produto mais barato foi {barato} que custa R${m:.2f}')
