from random import randint
sorteador = False
adivinhador = False
q = 0
palpites = []

min = int(input('Digite o valor mínimo: '))
max = int(input(f'Digite o valor máximo(Ele deve ser pelo menos {min+100}): '))
while max < min+100:
    max = int(input(f'Digite o valor máximo(Ele deve ser pelo menos {min + 100}): '))

ver = int(input('Escolha como deseja jogar: [1]Sorteador [2]Adivinhador: '))
while ver <1 or ver >2:
    ver = int(input('Digite uma opção válida: [1]Sorteador [2]Adivinhador: '))
if ver == 1:
    sorteador = True
else:
    adivinhador = True

if adivinhador:
    r = randint(min,max)
    acerto = False
    while not acerto:
        v = int(input('Qual é o seu palpite? '))
        q += 1
        palpites.append(v)
        if v > r :
            print('Menos... Tente novamente')
        if v < r:
            print('Mais... Tente novamente')
        if v == r:
            acerto = True
    print(f'Parabéns, você acertou depois de {q} tentativas, e seus palpites foram: {palpites}')

if sorteador:
    print(f'Pense em um número entre {min} e {max}')
    acerto = False
    while not acerto:
        v = randint(min,max)
        q +=1
        palpites.append(v)
        print(f'O computador escolheu {v}')
        resp = str(input('O palpite está certo[C] ou errado?[E]')).strip().upper()[0]
        if resp == 'C':
            acerto = True
        else:
            resp2 = int(input('A resposta é MAIOR [0] ou MENOR[1] que o palpite? '))
            if resp2 == 0:
                print('Mais... Tente novamente')
                min = v+1
            if resp2 == 1:
                print('Menos... Tente novamente')
                max = v-1
    print(f'O computador acertou depois de {q} tentativas e os palpites foram: {palpites}')