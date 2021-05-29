from collections import Counter
n,k=map(int,input().split())
cnt=0
s=input()
for i in range(k):
    a={}
    for j in s[i::k]:
        if j not in a:
            a[j]=1
        else:a[j]+=1
    a_s=sorted(a.items(),key=lambda x:x[1])
    cnt+=n//k-a_s[-1][1]
print(cnt)