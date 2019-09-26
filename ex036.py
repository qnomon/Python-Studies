vc = float(input('Digite o valor da casa:R$ '))
sal = float(input('Digite o valor do seu salário: '))
ano = int(input('Digite em quantos anos irá pagar: '))
parcela = ano*12
valpar = vc / parcela
if valpar > (0.3*sal):
    print(f'Seu emprestimo foi negado')
else:
    print(f'A casa no valor de R${vc:.2f} foi aprovada e voce dele pagar R${valpar:.2f} em {parcela} parcelas')