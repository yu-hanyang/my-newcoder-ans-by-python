for _ in range(int(input())):
    a,b=input().split()
    a10=int(a,16)
    b10=int(b,16)


    a_=[]
    b_=[]
    t=0
    while t==0:
        if a10 in b_:
            print(a10)
            t=1
            break
        elif b10 in a_:
            print(b10)
            t=1
            break
        else:
            if a10!=1:
                if a10%2==1:
                    a_.append(a10)
                    a10=(a10-1)//2
                else:
                    a_.append(a10)
                    a10=a10//2

            if b10!=1:

                if b10%2==1:
                    b_.append(b10)
                    b10=(b10-1)//2
                else:
                    b_.append(b10)
                    b10=b10//2


