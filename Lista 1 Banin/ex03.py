peso = float(input('Digite o peso do lutador: '))
if peso < 65:
    print('Valor inválido')
if peso >= 65 and peso <70:
    print('Peso Leve')
elif peso >= 70 and peso <75:
    print('Peso Ligeiro')
elif peso >=75 and peso <83:
    print('Peso Meio Médio')
elif peso >=83 and peso <91:
    print('Peso Médio')
elif peso >= 91 and peso <100:
    print('Peso Meio Pesado')
elif peso >100:
    print('Peso Pesado')
