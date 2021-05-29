n=int(input())
md=998244353
if n==3:
    print(0)
elif n < 4 :
    print(1)
else:
    if n&1:
        cnt=0
        type_2=(n-1)//4
        type_1=(n-1)%4
        cnt+=2**type_2