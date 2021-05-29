s=input().split('0')
t=0
flag=0
f=0
for i,j in enumerate(s):

    if j!='':
        t+=1
    if i!=0 and flag==0:

        if j!='' and s[i-1]!='':
            flag=1
    if j=='1':
        f=1



print(t-max(flag,f))
print(s,t)

