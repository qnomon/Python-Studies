cid = str(input('Digite o nome da cidade: ')).strip()
spl = cid.split()
print(f'A cidade {cid}, começa com santo ?')
print('santo'in spl[0].lower())

