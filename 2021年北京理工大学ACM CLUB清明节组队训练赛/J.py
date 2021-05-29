c,e,m=map(int,input().split())
if c==4 and (not e&1) and e*m!=0:
    e_2=e//2
    t=0
    for i in range(1,e_2//2+1):
        if i*(e_2-i)==m:
            print((e_2-i)+2,i+2)
            t=1
            break
        elif i*(e_2-i)>m:
            break

    # for i in range(1,int(m**0.5)+1):
    #     if m%i==0:
    #         j=m//i
    #         if j+j+i+i==e:
    #             print(j+2,i+2)
    #             break
    if t==0:
        print('impossible')
elif c==4 and e==0 and m==0:
    print(2,2)
elif c==4 and (not e&1) and m==0:
    print(e//2+2,2)
else:print('impossible')