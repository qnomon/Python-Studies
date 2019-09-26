lista = []
while True:
    v = int(input('Digite um valor [0 Ou menos para parar]: '))
    if v <= 0:
        break
    lista.append(v)

print(f'A lista gerada foi {lista}')