n=int(input())
a=list(map(int,input().split()))
md=1000000007
a.sort(reverse=True)
num_s=0
num_add=0
for i in a:
    num_s+=pow(i,2)
    num_add+=i
cnt=0
for i in range(n):
    temp_s=pow(a[i],2)
    temp_add=a[i]
    num_s-=temp_s
    num_add-=temp_add
    cnt=(cnt+((n-1-i)*temp_s+num_s-2*temp_add*num_add))%md
print(cnt)