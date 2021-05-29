sc=[198,88,28,6,328,648,1]
yhq=[128,58,28,18,198,388,8]
n=int(input())
out=0
for i in range(7):
    if n>=sc[i]:
        n-=sc[i]
        out+=(sc[i]*10+yhq[i])

print(out+n*10)