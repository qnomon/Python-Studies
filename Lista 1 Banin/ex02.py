n = 0
par = 0
impar = 0
while True:
    n = int(input('Digite um número [Digite 0 para parar]:'))
    if n == 0:
        break
    if n % 2 == 0:
        par += n
    else:
        impar += n

print(f'A soma dos números pares digitados é de {par}')
print(f'A soma dos números impares digitados é de {impar}')
