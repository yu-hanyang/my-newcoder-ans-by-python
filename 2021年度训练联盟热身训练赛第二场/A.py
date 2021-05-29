import math
for _ in range(int(input())):
    n=int(input())
    print('Input value:',n)
    if math.log(n,2)%1==0:
        print(n)
        print()
    else:
        print(2**(int(math.log(n,2))+1))
        print()
