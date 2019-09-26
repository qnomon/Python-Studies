'''sexo = ' '
while not sexo in 'MmFf':
    print('Por favor Digite um sexo válido.')
    sexo = str(input('Digite o sexo, apenas [M/F]: ')).upper()
print('Fim')'''

sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'mMfF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()