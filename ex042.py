a = float(input('Digite o comprimento da reta A: '))
b = float(input('Digite o comprimento da reta B: '))
c = float(input('Digite o comprimento da reta C: '))
if (b-c)<a<(b+c) and (a-c)<b<(a+c) and (a-b)<c<(a+b):
    print('Essas retas podem formar um triângulo.')
    if a == b == c :
        print('O triangulo formado será um triângulo EQUILÁTERO')
    elif a == b or b == c or a == c:
        print('O triangulo formado será um triâmgulo ISÓSCELES')
    else:
        print('O triângulo formado será um triângulo ESCALENO')
else:
    print('Não pode ser formado um triângulo')