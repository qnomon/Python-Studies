n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
c = 0
total = 0 #controladores termos adicionais
mais = 9 #controladores
while mais != 0 : #aninhamento de while
    total = total + mais #total recebe o termo a mais que o usuário deseja
    while c <= total:
        pa = n + (r*c)
        print(pa, end=' → ')
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'A progressão foi finalizada com {total} termos mostrados')
