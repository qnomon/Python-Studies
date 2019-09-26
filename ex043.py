peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em metros: '))
calculo = peso/(altura**2)
if calculo < 18.5 :
    print(f'O seu IMC é de {calculo:.2f} e você esta Abaixo do peso')
elif 18.5 <= calculo < 25 :
    print(f'O seu IMC é de {calculo:.2f} e você esta no peso ideal')
elif 25 <= calculo < 30 :
    print(f'O seu IMC é de {calculo:.2f} e você esta com sobrepeso')
elif 30 <= calculo < 40:
    print(f'O seu IMC é de {calculo:.2f} e você esta com Obesidade')
else:
    print(f'O seu IMC é de {calculo:.2f} e você esta com Obesidade Mórbida')