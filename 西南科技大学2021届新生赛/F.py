md=998244353
for _ in range(int(input())):
    n=int(input())
    out=((n*(n+1)*(2*n+1))%md)//3-(((1+n)*n)%md)//2
    print(out%md)
