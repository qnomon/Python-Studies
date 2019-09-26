lista = list ()
for c in range (0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-'*30)
print(f'Os números digitados foram {lista}')
for c, v in enumerate (lista):
     if c == 0:
         m = n = v
     if v >= m:
         m = v
     if v <= n:
         n = v
print(f'O maior valor encontrado foi {m} nas posições ', end='')
for c, v in enumerate (lista):
    if v == m:
        print(f'{c}...', end=' ')
print(f'\nO menor valor encontrado foi {n} nas posições ', end='')
for c, v in enumerate(lista):
    if v == n:
        print(f'{c}...', end=' ')