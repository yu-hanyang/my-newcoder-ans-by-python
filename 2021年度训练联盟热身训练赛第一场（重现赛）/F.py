m=int(input())
a=[]
for _ in range(m):
    a.append(int(input()))
a.sort()
s=[a[0]]
for i in range(1,m):
    s.append(s[i-1]+a[i])
i=0
while i<m-1.5:
    if i%1==0.5:
        if s[int(i-0.5)]==s[-1]-s[int(i+0.5)]:
            print(a[int(i+0.5)])
            break
    else:
        if s[int(i)]==s[-1]-s[int(i)]:
            if a[int(i)]==a[int(i)+1]:
                print(a[int(i)])
            else:
                print(a[int(i)]+1)
            break
    i+=0.5