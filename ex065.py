n = n1 = c = s = m = mn = 0
cont = 'S'
while cont in 'S':
    n = int(input('Digite um número para somar: '))
    s += n
    c += 1
    if c == 1:
        m = mn = n
    if n > m:
        m = n
    if n < mn:
        mn = n
    cont = str(input('Você deseja continuar? [S/N]: ')).upper()
print(f'A soma de todos os {c} números é igual a {s} e sua média é de {s / c:.2f}')
print(f'O menor número foi {mn} e o maior {m}')