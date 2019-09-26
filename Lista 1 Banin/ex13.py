x = float(input('Digite um valor [0]Para encerrar o programa: '))
tot = 0
while x != 0:
    tot +=x
    x = float(input('Digite um valor [0]Para encerrar o programa: '))
print(f'O total da soma dos números inseridos é de {tot}')