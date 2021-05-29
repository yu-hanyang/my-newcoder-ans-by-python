for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=[]
    t=0
    if n<3:
        print('No')
    else:
        for i in range(1,n-1):
            if a[i]>a[i-1] and a[i]>a[i+1]:
                k.append(i)
            if a[i]==a[i-1] or a[i]==a[i+1]:
                t=1

    if len(k)!=1 or t==1:
        print('No')
    elif a[n-1]>a[n-2] or a[0]>a[1]:
        print('No')

    else:
        print('Yes')


