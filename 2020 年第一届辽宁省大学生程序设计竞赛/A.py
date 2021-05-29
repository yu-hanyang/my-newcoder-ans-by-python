for _ in range(int(input())):
    n=int(input())
    d={}
    for i in range(3*n):
        s,a=input().split()
        d[s]=int(a)
    temp=sorted(d.items(),key=lambda x:x[1])
    for i in range(n):
        print('ACM-%d %s %s %s'%(i,temp[i*3][0],temp[i*3+1][0],temp[i*3+2][0]))
