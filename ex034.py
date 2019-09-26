atual = float(input('Digite o seu salário atual: R$'))
if atual >= 1250:
    p = 0.1
else:
    p = 0.15
aumento = (atual*p)+atual
print(f'Seu novo salário é de R${aumento:.2f}')