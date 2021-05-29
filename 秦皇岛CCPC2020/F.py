
for _ in range(int(input())):
    n,k=map(int,input().split())

    if k==1 or k>30:
        print('Case '+'#'+str(_+1)+': '+str(n))
    else:

        a = 0
        for i in range(1,n+1):
            if i==1:
                continue
            if pow(i,k)<=n:
                a+=((pow(i,k)-pow(i-1,k))//(i-1)+1)
            else:



        print('Case '+'#'+str(_+1)+': '+str(a))