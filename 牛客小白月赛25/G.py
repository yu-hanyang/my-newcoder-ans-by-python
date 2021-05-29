import math
a,b,c=map(int,input().split())
l=c
r=0
while r<l:
    mid=(r+l)/2
    f=mid**a+b*(math.log(mid))
    if abs(f-c)<0.00000001:
        break
    else:
        if f>c:
            l=mid
        else:r=mid
print(mid)
