from random import randint
r = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
c = 0
while True:
    if c > 4:
        break
    if c == 0:
        m = n = r[c]
    if r[c] > m:
        m = r[c]
    if r[c] < n:
        n = r[c]
    c += 1
print(f'Os números sorteados foram {r}\nO maior número sorteado foi {m} e o menor foi {n}')
