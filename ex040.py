n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nova: '))
media = (n1 + n2) / 2
if media < 5 :
    print(f'Sua média foi de {media:.1f} e você esta\033[31m REPROVADO')
elif media <= 6.9 :
    print(f'Sua média foi de {media:.1f} e você esta de\033[33m RECUPERAÇÃO')
else:
    print(f'Sua média foi de {media:.1f} e você esta\033[34m APROVADO')