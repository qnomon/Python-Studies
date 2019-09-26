'''from unidecode import unidecode

inp = input('Digite uma frase: ')

frasesa = unidecode(inp)
frasesp = frasesa.lower().split()
frase = ''.join(frasesp)

if frase[::-1] == frase:
    print(f'A frase "{inp}" é um palíndromo.')
else:
    print(f'A frase "{inp}" não é um palíndromo.')'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')