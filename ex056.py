somaidade = 0 #Soma de Todas as Idades
mediaidade = 0 #Média de todas as idades
mih = 0 # Maior idade para Homens
nomev = '' #Nome do Homem Mais velho
totm20 = 0 # Total de Mulheres com Menos de 20 anos
for p in range(1,5):
    print(f'-----{p}ª Pessoa-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm' : #Se for a primeira rodada do laço mih e nomev recebem os atributos
        mih = idade
        nomev = nome
    if sexo in 'Mm' and idade > mih: #Se o sexo for masculino e a idade for maior que a idade salva trocam-se os atributos
        mih = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20: #Se o sexo for feminino e a idade for abaixo de 20 anos se adiciona um no contador.
        totm20 += 1
mediaidade = somaidade /4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {mih} anos e se chama {nomev}')
print(f'Ao todo são {totm20} mulheres com menos de 20 anos')