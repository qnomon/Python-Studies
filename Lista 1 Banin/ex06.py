n = int(input('Digite quantos números quer inserir: '))
c = t = 0
while c < n:
    v = float(input('Digite um número real: '))
    if v > 0:
        t += v
    c += 1
print(f'O total dos valores positivos digitados é de {t}')
