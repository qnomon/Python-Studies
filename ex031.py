d = float(input('Digite a distancia em KM a ser percorrida: '))
if d <= 200:
    v = d*0.5
else:
    v = d*0.45
print(f'O valor a ser pago é de R${v:.2f}')