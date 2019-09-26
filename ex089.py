alunos = list()
media = 0
t = 0
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2)/2
    alunos.append([nome,[nota1,nota2],[media]])
    t += 1
    cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if cont not in 'SN':
        while cont not in 'SN':
            cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if cont == 'N':
        break
print('No. Nome               Média')
print('-'*30)
for c in range (0,t):
        print(f'{c}  {alunos[c][0]:.<20}{alunos[c][2]:.1f}')
while True:
    print('-' * 50)
    cont = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
    if cont == 999:
        break
    print('-'*50)
    print(f'O aluno {alunos[cont][0]}, tirou as notas {alunos[cont][1]}')
print('Programa encerrado, Volte sempre')
