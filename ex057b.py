s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
val = ['MF']
while s not in val :
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()[0]