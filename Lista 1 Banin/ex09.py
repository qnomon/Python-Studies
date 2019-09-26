n = int(input('Digite quantos números quer inserir: '))
c = 0
while c < n:
    v = float(input('Digite um valor: '))
    if c == 0:
        maior = menor = v
    if v > maior:
        maior = v
    if v < menor:
        menor = v
    c +=1
print(f'O Menor valor inserido foi {menor} e o Maior foi {maior}')

