n,k=map(int,input().split())
a=list(map(int,input().split()))
out=[]
aa=list(map(int,set(sorted(a))))
print(aa)
if k not in a:
    print(*a)
else:
    t=0
    wz_k=aa.index(k)
    while wz_k<len(aa)-1:
        if aa[wz_k+1]==aa[wz_k]+1 :

            t+=1
            wz_k+=1
        else:break
    t+=1
    for i in a:
        if i-t>0:
            out+=(i-t),
        else:
            out+=0,
    print(*out)
