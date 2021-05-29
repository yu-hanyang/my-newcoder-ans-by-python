for _ in range(int(input())):
        a=input()
        b=input()
        if '1' not in b:
            print(0)
        else:
            c=bin(int(a,2)^int(b,2))[2:]
            start=1+len(a)-len(c)





            t=0

            wz=[start]
            # while str(t) in str(c)[p:]:
            #     p=str(c)[p:].index(str(t))
            #     wz.append(start+p)
            #     t=1-t



            for i in range(len(c)):
                if c[i]==str(t):
                    wz.append(i+start)
                    t=1-t



            wz2=[0]
            start2=1
            t2=1
            for i in range(len(b)):
                if b[i]==str(t2):
                    wz2.append(i+start2)
                    t2=1-t2
            if len(wz)>len(wz2):
                print(*wz2)
            else:
                print(*wz)

