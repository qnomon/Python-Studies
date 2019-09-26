'''lista = str(input('Digite a expressão: '))
c1 = lista.count('(')
c2 = lista.count(')')
if c1 == c2:
    print('Sua expressão esta Correta! ')
else:
    print('Sua expressão esta Errada!')''' #esse algoritimo não resolve ) fechado antes de aberto(
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')


