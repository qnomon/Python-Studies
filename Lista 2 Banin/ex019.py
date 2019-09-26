lista = list()
v = 1
c = 0
while True:
    v = int(input('Digite um valor: '))
    if v <=0:
        break
    if c == 0 or v > lista[len(lista)-1]:
        lista.append(v)
        print('Valor inserido no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos,v)
                print(f'Valor inserido na posição {pos}')
                break
            pos += 1
    c +=1
print(f'Os valores digitados na ordem foram {lista}')