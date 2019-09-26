n = 0
n1 = 0
c = 0
s = 0
n = int(input('Digite um número pra somar, digite 999 para parar: '))
while n != 999:
    s += n +n1
    c += 1
    n = int(input('Digite um número pra somar, digite 999 para parar: '))
print(f'A soma total foi de {s} de {c} diferentes números')