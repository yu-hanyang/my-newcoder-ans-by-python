md=1000000007
for _ in range(int(input())):
    n=int(input())
    out=0
    l=len(str(n))-1

    while l>0:
        to=n//pow(10,l)
        bj=l*pow(10,l-1)
        yu=n%pow(10,l)
        out+= bj*to
        if to>7:
            out+=pow(10,l)
        elif to==7:
            out+=yu+1
        n=yu
        out=out%md



        l=len(str(n))-1
    if n%10>=7:
        out+=1
    print(out)


