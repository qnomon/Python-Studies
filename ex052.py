v = int(input('Digite um valor: '))
validador = 0
for c in range(1, v):
    if v % c == 0:
        validador += 1
if validador > 1:
    print(f'\033[31mEsse número NÃO é primo, pois é divisível por {validador+1} números diferentes ')
else:
    print('\033[34mEsse número é primo')