from random import choice

a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))

r = (choice([a1, a2, a3, a4]))
print (f'O aluno que deverá apagar o quadro é: {r}')

