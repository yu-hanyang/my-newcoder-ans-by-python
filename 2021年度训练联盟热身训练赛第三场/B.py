import math
n,m=map(int,input().split())
g=math.gcd(n,m)
if (m//g)%2==1 and (n//g)%2==1:
    print(g)
else:
    print(0)