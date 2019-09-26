import math

c1 = float(input('Digite o cateto oposto: '))
c2 = float(input('Digite o cateto adjacente: '))
hip = math.hypot(c1, c2)
print(f'A hipotenusa do triangulo retangulo composto por {c1} e {c2} é de {hip:.3f}')
