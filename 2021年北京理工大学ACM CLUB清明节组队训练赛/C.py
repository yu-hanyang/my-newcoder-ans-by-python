n,p=map(int,input().split())
tmp=0
t=0
pm=[]
for i in range(n):
    s=int(input())
    if s<tmp:
        t+=1
    pm+=(p-t),

    tmp=s

if n==1 and p==1:
    print(0 if s==0 else 1)
elif n==1:
    print(0 if s==0 else 'ambiguous')
elif p==1 and t==0:
    if s==0:
        for i in range(n):
            print(0)
    else:
        for i in range(n):
            print(1)

elif s==0 and t==p:
    for i in pm:
        print(i)
elif t==p-1 and s!=0:
    for i in pm:
        print(i)
else:
    print('ambiguous')

