from time import sleep
def maior(*num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for r in num:
        print(r, end=' ')
        sleep(0.3)
    for v in num:
        if cont == 0:
            maior = v
        if v > maior:
            maior = v
        cont +=1
    print(f'Foram informados {cont} valores e o maior valor foi {maior}')



maior(2,9,4,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()