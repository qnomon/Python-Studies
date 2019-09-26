p = 0
matriz = [ [0,0,0],[0,0,0],[0,0,0] ]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=(int(input(f'Digite o valor para [{l},{c}]: ')))
print('=-' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=(' '))
    print()
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            p += matriz[l][c]
c3 = (matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])
for l in range(0,3):
    if l == 0:
        m = matriz[1][l]
    if m < matriz[1][l]:
        m = matriz[1][l]
print('=-'*30)
print(f'A soma de todos os valores pares é igual a {p}\nA soma dos valores da terceiraa coluna é igual a {c3}')
print(f'O maior valor da segunda linha é {m}')