n = int(input('Digite quantos números quer inserir: '))
c = vali = 0
while vali < n:
    v = float(input('Digite um valor: '))
    if v >= 0 :
        if c == 0:
            maior = menor = v
        if v > maior:
            maior = v
        if v < menor:
            menor = v
        c +=1
        vali += 1
    else:
        vali +=1
print(f'O Menor valor inserido foi {menor} e o Maior foi {maior}')


