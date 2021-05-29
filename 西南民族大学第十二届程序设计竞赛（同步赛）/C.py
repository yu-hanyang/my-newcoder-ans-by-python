n,m=map(int,input().split())
ls=[]
for i in range(n):
    u,v,w=map(int,input().split())
    if u==0:
        ls.append([u,v,w])
ls.sort(key=lambda x:x[2],reverse=True)
max1=ls[0][2]
min1=n
j=0
while ls[j][2]==max1:
    min1=min(min1,ls[j][1])
    j+=1
print(max1,min1)
