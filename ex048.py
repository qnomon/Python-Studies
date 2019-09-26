t = 0
cont = 0
for c in range(3, 500, 3):
    if c% 2 == 1:
        cont = cont +1
        t += c
print(f'A soma de todos os {cont} valores impares multiplos de 3 entre 3 e 500 é igual a {t}')