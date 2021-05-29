import time
t1=time.time()
cnt=0
ls={}
for i in range(1,1000000+1):
    if '1' in str(i):
        cnt+=str(i).count('1')
        ls[i]=cnt
t2=time.time()
print(ls)