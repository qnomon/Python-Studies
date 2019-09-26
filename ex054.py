from datetime import date
maiores = 0
menores = 0
for c in range(0, 7):
    datas = int(input('Digite o ano de nascimento: '))
    if date.today().year - datas >= 21:
        maiores += 1
    elif date.today().year - datas < 21:
        menores += 1
print(f'{maiores} pessoas ja atingiram a maioridade e {menores} pessoas ainda não atingiram a maioridade')