a=input()
b=input()
l=min(len(a),len(b))
out=''
t=0
if a=='0':
    print(b)
elif b=='0':
    print(a)
else:
    for i in range(l):
        n=int(a[-1-i])+int(b[-1-i])
        out=str(n%10)+out
    if len(a)>len(b):
        out=a[:-l]+out
        print(out,1)
    elif len(a)<len(b):
        out=b[:-l]+out
        print(out,2)
    else:
        print(int(out))