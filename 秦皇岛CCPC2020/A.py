import math

def C(x):
    return x*(x-1)//2

for _ in range(int(input())):
    r,b=map(int,input().split())
    # if r < 2:
    #     print('Case '+'#'+str(_+1)+': '+'0/'+str(1))
    # else:
    fz=C(r)
    fm=C(r+b)
    g=math.gcd(fz,fm)

    print('Case '+'#'+str(_+1)+': '+str(fz//g)+'/'+str(fm//g))

