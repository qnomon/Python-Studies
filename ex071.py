saque = int(input('Digite o valor que deseja sacar: '))
cedulas = [1, 10, 20, 50]
c = 3
while saque > 0:
    qntcedulas = saque // cedulas[c]
    saque -= qntcedulas * cedulas[c]
    if qntcedulas > 0:
        print(f'{qntcedulas} cédulas de {cedulas[c]}')
    c -= 1