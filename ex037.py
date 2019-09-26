import math
num = int(input('Digite um numero '))
conv = int(input('Digite [1] para converter para binário\n[2] para converter para octal\n[3] para converter para hexadecimal: '))
b = str (bin(num))
oc = str (oct(num))
he = str(hex(num))
if conv == 1:
    print(f'O número digitado foi {num},e sua conversão binária é {b[2:]}')
elif conv == 2:
    print(f'O número digital foi {num}, e a sua conversão octal é {oc[2:]}')
elif conv == 3:
    print(f'O número digital foi {num}, e a sua conversão hexadecimal é {he[2:]}')
else:
    print('Por favor digite um valor de conversão válido.')
