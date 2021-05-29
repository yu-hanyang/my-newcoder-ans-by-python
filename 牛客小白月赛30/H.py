n,m,k=map(int,input().split())
a=list(map(int,input().split()))
aa=sorted(a)[:k]
for i in range(m):
    s=input().split()
    if s[0]=='2':
        print(aa[-1])
    else:
        if int(s[-1])<aa[-1]:
            for i in range(k):
                if aa[i]>int(s[-1]):
                    aa.insert(i,int(s[-1]))
                    break
            aa.pop()