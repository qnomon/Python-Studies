a = float(input('Digite o comprimento da reta A: '))
b = float(input('Digite o comprimento da reta B: '))
c = float(input('Digite o comprimento da reta C: '))
if (b-c)<a<(b+c) and (a-c)<b<(a+c) and (a-b)<c<(a+b):
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')
