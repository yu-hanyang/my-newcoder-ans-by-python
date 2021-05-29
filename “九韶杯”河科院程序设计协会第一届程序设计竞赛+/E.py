md=1000000007
cnt=0
cnt_1=0
temp=0
for i in range(1,20210411+1):
    cnt+=((1+i)*i)//2
    temp+=i//2
    cnt_1+=temp
print((cnt+cnt_1))
