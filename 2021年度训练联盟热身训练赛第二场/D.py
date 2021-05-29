for _ in range(int(input())):
    g,c=map(int,input().split())
    gloup=list(input().split())
    gloup.sort()
    d={}
    for i in gloup:
        d[i]=[0]*6
    for i in range(c):
        g1,goat1,g2,goat2=input().split()
        if int(goat1)>int(goat2):
            d[g1][0]+=3
            d[g1][1]+=1
            d[g2][2]+=1
            d[g1][4] += int(goat1)  # g1进球数
            d[g2][5] += int(goat1)  # g2对手进球数
            d[g2][4] += int(goat2)
            d[g1][5] += int(goat2)
        elif int(goat1)<int(goat2):
            d[g2][0]+=3
            d[g2][1]+=1
            d[g1][2]+=1
            d[g2][4] += int(goat2)
            d[g1][5] += int(goat2)
            d[g1][4] += int(goat1)  # g1进球数
            d[g2][5] += int(goat1)  # g2对手进球数
        elif int(goat1)==int(goat2):
            d[g1][0]+=1
            d[g1][3]+=1
            d[g1][4]+=int(goat1)#g1进球数
            d[g2][5]+=int(goat1)#g2对手进球数
            d[g2][0]+=1
            d[g2][3]+=1
            d[g2][4]+=int(goat2)
            d[g1][5]+=int(goat2)
    mz=sorted(list(d.items()),key= lambda x:x[0])
    zf=sorted(mz,key=lambda x:(x[1][0],x[1][4]-x[1][5],x[1][4]),reverse=True)
    print('Group',_+1,end='')
    print(':')
    for i in zf:
        print(i[0],end=' ')
        print(*i[1])
    print()