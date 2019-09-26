v = int(input('Digite um valor: '))
validador = 0
contador = 1
while contador < v:
    if v % contador == 0:
        validador += 1
    contador +=1
if validador > 1:
    print(f'Esse número NÃO é primo, pois é divisível por {validador+1} números diferentes ')
else:
    print('Esse número é primo')