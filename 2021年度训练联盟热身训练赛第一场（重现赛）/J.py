n=int(input())
s=[]
t=0
for i in range(n):
    a=input()
    if a.count('W')!=(n//2):
        t=1
        break
    if ('WWW' in a) or ('BBB' in a):
        t=1
        break
    s.append(a)

if t==1:
    print(0)
else:
    for i in range(1,n-1):
        for j in range(n):
            if s[i-1][j]==s[i][j]==s[i+1][j]:
                t=1
                break
        if t==1:
            break
    if t==1:
        print(0)
    else:
        print(1)