from random import randint
p = int(input('Digite \n[1] para escolher Pedra, \n[2] para escolher Papel e \n[3] para escolher Tesoura: '))
m = randint(1, 3)
if p == m :
    print('\033[33mEmpate') #condicional de empate
elif p == 1 and m == 3 :
    print('Você escolheu Pedra e \033[34mVenceu') # Condicional para vitória escolhendo pedra
elif p == 1 and m == 2 :
    print('Você escolheu Pedra e \033[31mPerdeu') # Condicional para derrota escolhendo pedra
elif p == 2 and m == 1 :
    print('Você escolheu Papel e \033[34mVenceu') # Condicional para vitória escolhendo Papel
elif p == 2 and m == 3 :
    print('Você escolheu Papel e \033[31mPerdeu') # Condicional para derrota escolhendo Papel
elif p == 3 and m == 2 :
    print('Você escolheu Tesoura e \033[34mVenceu') #Condicional para vitória escolhendo Tesoura
elif p == 3 and m == 1:
    print('Você escolheu Tesoura e \033[31mPerdeu') #Condicional para derrota escolhendo Tesoura
else:
    print('Escolha apenas valores entre 1 e 3') # condicional de valores incorretos