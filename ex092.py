from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - ano
ctps = int(input('CTPS: '))
if ctps != 0:
    cadastro['ctps'] = ctps
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['contratação'] + 35 - ano
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')