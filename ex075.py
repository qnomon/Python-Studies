v = (int(input('Digite um valor: ')), int(input('Digite um outro valor: ')), int(input('Digite um outro valor: ')), int(input('Digite um outro valor: ')))
c = 0
print(f'O número 9 apareceu {v.count(9)} Vezes.')
if 3 in v:
    print(f'O primeiro número 3 apareceu na {v.index(3)+1}ª posição')
else:
    print(f'O número 3 não apareceu nenhuma vez')
print(f'Os números pares foram:', end=' ')
while True:
    if c > 3:
        break
    if v[c] % 2 == 0:
        print(f'{v[c]}', end=' ')
    c +=1