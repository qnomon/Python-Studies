a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
menor = a
# Verificando o menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
#Verificando o maior
if b > a and b > c:
    maior =b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}.\nO maior valor digitado foi {maior}.')