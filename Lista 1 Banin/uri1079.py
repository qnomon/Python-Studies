N = int(input())
m = 0
for c in range(0,N):
    a,b,c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    m = ((a*2)+(b*3)+(c*5))/(2+3+5)
    print('{:.1f}'.format(m))
