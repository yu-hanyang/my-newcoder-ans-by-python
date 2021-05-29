s=input()
temp=s[-1]
for i in s:
    if i!=temp:
        print(2)
        break
else:
    print(-1)