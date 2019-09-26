a = float(input())
b = 0
if a < 2000.0:
    print('Isento')
elif a >2000.0 and a <= 3000.0:
    b = ((a-2000)*0.08)
    print('R$ {:.2f}'.format(b))
elif a>3000.0 and a <= 4500.0:
    b = (((a//3000*3000)-2000)*0.08)+((a-3000)*0.18)
    print('R$ {:.2f}'.format(b))
elif a >4500:
    b = (1000*0.08)+(1500*0.18)+((a-4500)*0.28)
    print('R$ {:.2f}'.format(b))