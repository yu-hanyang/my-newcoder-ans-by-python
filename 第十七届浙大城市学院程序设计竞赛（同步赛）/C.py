for _ in range(int(input())):
    x,m,n=map(int,input().split())
    grdr=1
    zq=n//14
    bdzqdts=(n-7)%14
    kcr=0
    if n%14==0:
        print(0)
    else:
        jl=0
        for i in range(zq+1):
            grdr+=(7*pow(x,i))
            if grdr>m:
                grdr-=(7*pow(x,i))
                jl=i
                break
            if i==0:
                continue
        sg=m-grdr
        fsg = bdzqdts * pow(x, jl)
        if zq==0 and n<8:
            print(0)
        elif zq==0:
            print(1)
        elif jl<zq-1:
            print(0)

        else:
            print(min(sg,fsg))


