dias = int (input ('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados?  '))
t = (dias* 60) + (km*0.15)
print(f'O Total a ser pago é de R$ {t:.2f}')
