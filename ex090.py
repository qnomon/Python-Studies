aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
print(f'A situação é igual a {aluno["situacao"]}')