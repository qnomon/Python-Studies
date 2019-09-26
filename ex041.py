from datetime import  date
ano = int(input('Digite o ano do seu nascimento: '))
i = date.today().year
idade = i - ano
if idade <= 9:
    print(f'Você tem {idade} anos e pertence a categoria MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} anos e pertence a categoria INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos e pertence a categoria JÚNIOR')
elif idade <= 20:
    print(f'Você tem {idade} anos e pertence a categoria SÊNIOR')
else:
    print(f'Você tem a {idade} anos e pertence a categoria MASTER')