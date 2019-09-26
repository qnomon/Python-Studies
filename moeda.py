def aumentar(valor, porcentagem, format=False):
    t = valor + (porcentagem/100*(valor))
    if format:
        f = f'R${t:.2f}'
        return f
    else:
        return t


def diminuir(valor, porcentagem, format=False):
    t = valor - (porcentagem/100*(valor))
    if format:
        f = f'R${t:.2f}'
        return f
    else:
        return t


def dobro(valor, format=False):
    t = valor * 2
    if format:
        f = f'R${t:.2f}'
        return f
    else:
        return t


def metade(valor, format=False):
    t = valor/2
    if format:
        f = f'R${t:.2f}'
        return f
    else:
        return t


def moeda(msg):
    r = 'R$'
    t = f'{r}{msg:.2f}'
    return t


def resumo(valor,aum,red):
    print('-'*30)
    print('       Resumo do Valor')
    print('-'*30)
    print(f'Preço analisado: {moeda(valor):>13}')
    print(f'Dobro do preço: {dobro(valor,True):>14}')
    print(f'Medade do preço: {metade(valor,True):>13}')
    print(f'{aum}% de aumento: {aumentar(valor,aum,True):>14}')
    print(f'{red}% de redução: {diminuir(valor,red,True):>14}')
