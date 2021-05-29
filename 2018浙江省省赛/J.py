for _ in range(int(input())):
    n=int(input())
    s=input()
    out=''
    if (((1+n)*n)//2)%2==0:
        if n%2==0:
            t=0
            for i in range(n):
                if t==0 and s[i]=='1':
                    t=1-t
                    out+='3'
                elif t==0 and s[i]=='0':
                    t=1-t
                    out+='1'
                elif t==1 and s[i]=='1':
                    t=1-t
                    out+='4'
                else:
                    t=1-t
                    out+='2'
                if i==(n//2)-1:
                    t=1-t
        else:
            n=n-1
            t = 0
            for i in range(n ):
                if t == 0 and s[i] == '1':
                    t = 1 - t
                    out += '3'
                elif t == 0 and s[i] == '0':
                    t = 1 - t
                    out += '1'
                elif t == 1 and s[i] == '1':
                    t = 1 - t
                    out += '4'
                else:
                    t = 1 - t
                    out += '2'
                if i == (n//2)-1:
                    t=0
            if s[-1]=='0':
                out+='2'
            else:
                out+='4'
        print(out)

    else:
        print(-1)

for _ in range(int(input())):
    n=int(input())
    s=input()
    out=''
    if (((1+n)*n)//2)%2==0:
        if n%2==0:
            t=0
            for i in range(n):
                if t==0 and s[i]=='1':
                    t=1-t
                    out+='3'
                elif t==0 and s[i]=='0':
                    t=1-t
                    out+='1'
                elif t==1 and s[i]=='1':
                    t=1-t
                    out+='4'
                else:
                    t=1-t
                    out+='2'
                if i==(n//2)-1:
                    t=1-t
        else:
            n=n-1
            t = 0
            for i in range(n ):
                if t==0 and s[i]=='1':
                    t=1-t
                    out+='3'
                elif t==0 and s[i]=='0':
                    t=1-t
                    out+='1'
                elif t==1 and s[i]=='1':
                    t=1-t
                    out+='4'
                else:
                    t=1-t
                    out+='2'
                if i==(n//2)-1:
                    t=0
            if s[-1]=='0':
                out+='2'
            else:
                out+='4'
        print(out)

    else:
        print(-1)

