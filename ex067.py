while True:
    v = int(input('Digite um valor para saber sua tabuada: '))
    if v < 0:
        break
    for c in range(1, 11):
        print(f'{v} X {c:2} = {v * c:2}')
print('Programa tabuada encerrado..')