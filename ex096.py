def area(a,b):
    area = a*b
    print(f'A área de um terreno {a}x{b} é de {area}m².')


print('Controle de Terrenos')
print('-'*30)
a = float(input('Largur(m): '))
b = float(input('Comprimento(m): '))
area(a,b)