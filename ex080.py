lista = list()
for c in range(0,5):
    v = int(input('Digite um valor: '))
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
print('=-'*30)
print(f'Os valores digitados na ordem foram {lista}')