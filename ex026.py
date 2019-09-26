f = str(input('Digite uma frase: ')).strip()
count = f.lower().count('a')
pri = f.lower().find('a') +1
ult = f.lower().rfind('a') +1
print(f'Na frase {f}, existem {count} letras A')
print (f'O primeiro A se encontra na posição {pri}, e o último A na posição {ult}')
