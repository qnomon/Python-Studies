v = float(input('Digite o valor do produto '))
cond = int(input('Digite [1] para pagamento a vista com dinheiro ou cheque;\nDigite [2] para pagamento a vista no cartão\nDigite [3] para pagamento de 2x no cartão\nDigite [4] para pagamento 3x ou mais no cartão: '))
if cond == 1 :
    print(f'O valor a ser pago é de R${v-v*0.1:.2f}')
elif cond == 2 :
    print(f'O valor a ser pago é de R${v-v*0.05:.2f}')
elif cond == 3 :
    print (f'O valor a ser pago é de R${v:.2f} em 2x')
elif cond == 4 :
    print (f'O valor a ser pago é de R${v+v*0.2:.2f}')
else:
    print('Digite um valor válido de condição de pagamento')