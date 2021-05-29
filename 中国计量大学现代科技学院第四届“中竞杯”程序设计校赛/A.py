import math
def jc(x):
    if x==0:
        return 1
    else:
        out=1
        for i in range(1,x+1):
            out*=1
    return out
def C(n,m):
    if m==n or m==0:
        return jc(n)
    elif m==1 or m==n-1:
        return n
    else:
        fz=1
        fm=1
        for i in range(max(m,n-m)+1,n+1):
            fz*=i
        for i in range(1,min(m,n-m)+1):
            fm*=i
        return fz//fm
x_=[[1,1,1],[1,1,1],[1,1,1]]
y_=[[1,1,1],[1,1,1],[1,1,1]]
xd1=0
xd2=0
cout_0=0
a=0
for _ in range(3):
    n=input()
    for i in range(3):
        if n[i]=='.':
            x_[_][i]=0
            cout_0+=1
            y_[i][_]=0
            if _==0:
                if i==0:
                    xd1+=1
                elif i==2:
                    xd2+=1
            elif _==1:
                if i==1:
                    xd1+=1
                    xd2+=1
            elif _==2:
                if i==0:
                    xd2+=1
                elif i==2:
                    xd1+=1
if xd1==3:
    a+=1
if xd2==3:
    a+=1
for i in range(3):
    if sum(x_[i])==0:
        a+=1
    if sum(y_[i])==0:
        a+=1
if a==0:
    print(0)
else:
    b=C(cout_0,3)
    gd=math.gcd(a,b)
    a=a//gd
    b=b//gd

    print(a,b)
