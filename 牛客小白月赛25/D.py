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
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n):
