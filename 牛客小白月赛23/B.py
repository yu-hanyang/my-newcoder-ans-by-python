ls=[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200]
for _ in range(int(input())):
    p=int(input())
    ls=[]
    for i in range(1,int(p**0.5)+1):
        if p%i==0 :
            ls.append(i)
    if len(ls)==1:
        print(p//ls[-1])
    elif p//ls[-1]==ls[-1]:
        print(p//ls[-2])
    else:print(p//ls[-1])



