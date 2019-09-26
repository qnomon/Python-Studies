def leiaint():
    n = input('Digite um número: ')
    s = type(5)
    while n.isnumeric() == False:
        print('\033[31mERRO, digite um número inteiro\033[m')
        n = input('Digite um número: ')
    else:
        return f'\033[34m{n}\033[m'



n = leiaint()
print(f'Você acabou de digitar o número {n}')