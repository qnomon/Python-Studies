t = 0
for c in range(0,6):
    num = float(input())
    while num == 0:
        num = float(input())
    if num > 0:
        t +=1
print('{} valores positivos'.format(t))
