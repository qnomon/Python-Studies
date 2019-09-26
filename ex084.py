dados = list()
lista = list()
totleve = list()
totpesado = list()
c = 0
while True:
    lista.append(str(input('Digite o nome: ')))
    lista.append((float(input('Digite o peso: '))))
    dados.append(lista[:])
    lista.clear()
    c += 1
    cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('Deseja continuar?[S/N]: ')).strip.upper()
    if cont == 'N':
        break
for s in range (0, len(dados)):
    for p in dados:
        if s == 0:
            leve = p[1]
            pesado = p[1]
        if p[1] < leve:
            leve = p[1]
        if p[1] > pesado:
            pesado = p[1]
for v in dados:
    if v[1]== leve:
        totleve.append(v[0])
    if v[1] == pesado:
        totpesado.append(v[0])
print(f'Foram adicionados {c} pessoas no cadastro')
print(f'O maior peso registrado foi {pesado}Kg, Peso de: {totpesado}')
print(f'O menor peso registrado foi {leve}Kg, Peso de: {totleve}')
