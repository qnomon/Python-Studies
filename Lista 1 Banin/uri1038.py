entrada = str(input())
split = entrada.split()
cod = int(split[0])
qnt = int(split[1])
total = 0
if cod == 1:
    total = qnt * 4
elif cod == 2:
    total = qnt * 4.5
elif cod == 3:
    total = qnt * 5
elif cod == 4:
    total = qnt * 2
elif cod == 5:
    total = qnt * 1.5
print('Total: R$ {:.2f}'.format(total))