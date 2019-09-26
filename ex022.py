nome = str(input('Digite seu nome completo: '))
min = nome.lower()
mai = nome.upper()
q = len(nome.strip()) - nome.count(' ')
p = len(nome.split()[0])

print(f'Seu nome com todas as letras maiusculas {mai}\nSeu nome com todas as letras minúsculas {min}')
print(f'Seu nome completo tem {q} Caracteres desconsiderando os espaços\nSeu primeiro nome tem {p} letras')