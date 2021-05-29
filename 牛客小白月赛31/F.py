import math
for _ in range(int(input())):
    m=int(input())
    n=0
    t=0
    while t<m-n:
        t+=1
        n+=t
    if m==n:
        print(1)
    else:
        print((n*m)//math.gcd(n*m,n))