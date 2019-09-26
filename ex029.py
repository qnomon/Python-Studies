v = int(input('A qual velocidade o carro passou no radar? '))
m = (v-80)*7
if v > 80 :
    print(f'Você foi multado em R${m},00 ')
else:
    print('Você estava dentro do limite de velocidade.')