from random import randint
print('-=-'*10)
print('Vamos Jogar Par ou Ímpar')
print('-=-'*10)
c = 0
while True:
    r = randint(1,10)
    v = int(input('Digite um número para Jogar: '))
    e = str(input('Escolha Par ou Ímpar[P/I]')).strip().upper()
    s = r + v
    if e == 'P'and s % 2 == 0 :
        c += 1
        print('Você venceu, vamos jogar de novo!')
    if e == 'I' and s % 2 == 1:
        c +=1
        print('Você venceu, vamos jogar de novo!')
    if e == 'P' and s % 2 == 1:
        break
    if e == 'I' and s % 2 == 0:
        break
if c > 0:
    print(f'\033[31mGame Over\033[m, você venceu \033[34m{c}\033[m vezes !')
else:
    print('\033[31mGame Over\033[m, você não venceu nenhuma vez')


