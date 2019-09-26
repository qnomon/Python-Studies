tp = h = m = 0
while True:
    print('-'*20)
    print('Cadastre Uma Pessoa' )
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip().upper()
    while not sexo in 'MmFf':
        sexo = str(input('Sexo [M/F] ')).strip().upper()
    if idade >= 18:
        tp += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade <= 20:
        m+=1
    cont = str(input('Deseja Continuar?[S/N] ')).strip().upper()
    while not cont in 'SsNn':
        cont = str(input('Deseja Continuar?[S/N] ')).strip().upper()
    if cont == 'N':
        break
print('-'*20)
print('Programa Finalizado')
print('-'*20)
print(f'Total de pessoas com mais de 18 anos: {tp}\nAo todo temos {h} homens cadastrados\nE temos {m} mulheres com menos de 20 anos')