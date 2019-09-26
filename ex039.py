from datetime import  date
i = int(input('Digite o ano do seu nascimento: '))
ano = date.today().year
idade = ano - i
if idade == 18:
    print(f'Você tem {idade} anos e deve se alistar esse ano')
elif idade < 18:
    print(f'Você tem {idade} anos e faltam {18-idade} anos para se alistar')
else:
    print(f'Você tem {idade} anos e ja passaram {idade-18} anos da data de se alistar')