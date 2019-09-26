def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número n.
    """
    f = 1
    for c in range(n, 0 ,-1):
        if show:
            f *= c
            if c > 1:
                print(f' {c} ', end='x')
            else:
                print(f' {c} ', end='= ')
        else:
            f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)