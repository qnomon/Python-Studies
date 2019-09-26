p = float(input('Digite o peso: '))
maior = p
menor = p
for c in range(0,4):
    p = float(input('Digite o peso: '))
    if p < menor:
        menor = p
    elif p > maior :
        maior = p
print(f'O menor peso registrado foi {menor}Kg, e o maior foi {maior}Kg.')