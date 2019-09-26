pessoas = {}
todas = []
total = 0
while True:
    pessoas['nome']= str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if pessoas['sexo'] not in 'MF':
            print('Erro: Digite um sexo correto')
        else:
            break
    pessoas['idade'] = int(input('Idade: '))
    todas.append(pessoas.copy())
    cont = str(input('Deseja Continuar?[S/N]')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Foram cadastradas {len(todas)} pessoas')
for c in range(0,len(todas)):
    total += todas[c]['idade']
media = total/len(todas)
print(f'A média de idade do grupo é de {media}')
print(f'As mulheres do grupo são: ', end='')
for c in range(0,len(todas)):
    if todas[c]['sexo'] == 'F':
        print(f'{todas[c]["nome"]}',end= ' ')
print()
print(f'As pessoas acima da média de idade são: ', end='')
for c in range(0, len(todas)):
    if todas[c]['idade'] > media:
        print(f'{todas[c]["nome"]} com {todas[c]["idade"]} anos', end=' ')


