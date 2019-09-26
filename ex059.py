a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = 0
while c != 5:
    c = int(input(''''Escolha uma opção: 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa: '''))
    if c == 1:
        print(f'A o resultado da soma de {a} + {b} é igual a {a + b}.' )
    if c == 2:
        print(f'O produto da multiplicação de {a} e {b} é igual a {a*b}. ')
    if c == 3:
        if a > b:
            print(f'O Primeiro valor {a}, é maior que o segundo valor {b}')
        elif b > a:
            print(f'O Segundo valor {b}, é maior que o primeiro valor {a}')
        elif b == a:
            print(f'Os dois valores, {a} e {b}, são iguais')
    if c == 4:
        a = float(input('Digite o primeiro novo valor: '))
        b = float(input('Digite o segundo novo valor: '))
    if c > 5 or c < 1:
        print('Por favor digite uma operação válida')