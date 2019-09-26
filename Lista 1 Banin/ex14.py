x = float(input('Digite um valor [0]Para encerrar o programa: '))
tot = c = 0
while x != 0:
    tot +=x
    c += 1
    x = float(input('Digite um valor [0]Para encerrar o programa: '))
med = tot/c
print(f'O total da soma dos {c} números inseridos é de {tot} e sua média é de {med}')