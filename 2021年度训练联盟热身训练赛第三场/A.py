n=int(input())
a=input().split()
b=input().split()
x=-1
y=-1
out=[]
t=0
for i in b:
    if i<='Z' and i>='A':
        if t%2==0:
            if a[t]=='T':
                x=1
            else:
                x=0
        else:
            if a[t]=='T':
                y=1
            else:
                y=0
        t+=1
    elif i=='*':
        if x!=-1 and y!=-1:
            out+=(x&y),
            x=-1
            y=-1
        elif y==-1:
            out+=(out[-1]&x),
        else:
            out+=(out[-1]&out[-2]),
    elif i=='+':
        if x!=-1 and y!=-1:
            out+=(x|y),
            x=-1
            y=-1
        elif y==-1:
            out+=(out[-1]&x),
        else:
            out+=(out[-1]|out[-2]),

    elif i == '-' and y!=-1:
        y=1-y
        x=1-x
    elif i=='-' and x!=-1:
        x=1-x
    elif i == '-' and len(out)>0:
        out[-1]=1-out[-1]
if len(out)==0:
    if y==-1 and x==1:
        print('T')
    elif y==-1 and x==0:
        print('F')
    elif x==0:
        print('F')
    else:
        print('T')

elif out[-1]==0:
    print('F')
else:
    print('T')
