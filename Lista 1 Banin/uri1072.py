N = int(input())
i = o = 0

for c in range(0,N):
    X = int(input())
    if X >=10 and X <=20:
        i += 1
    else:
        o += 1
print('{} in'.format(i))
print('{} out'.format(o))