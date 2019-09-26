lista = list()
NEG = list()
POS = list()


num = -1

while num < 0 or num > 50:
    num = int(input('Digite um número entre 0 e 50: '))

for x in range (0,num):
    a = float(input('Digite um valor: '))
    lista.append(a)

for x in lista:
    if x < 0:
        NEG.append(x)
    else:
        POS.append(x)

print(f'A lista dos positivos é {POS} e contém {len(POS)} elementos.')
print(f'A lista dos negativos é {NEG} e contém {len(NEG)} elementos.')

