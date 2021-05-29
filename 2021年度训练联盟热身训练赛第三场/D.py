a=1
b=1
t=0
for _ in range(int(input())):
    b=int(input())
    while a<b:
        print(a)
        t=1
        a+=1
    a+=1
if not t:
    print('good job')