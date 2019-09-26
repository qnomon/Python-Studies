import math

num = float(input('Digite um ângulo: '))
n = math.radians(num)
sen = math.sin(n)
cos = math.cos(n)
tan = math.tan(n)
print(f'O seno de {num}° é igual a {sen:.4f}\nO cosseno de {num}° é igual a {cos:.4f}\nA tangente de {num}° é igual {tan:.4f}')

