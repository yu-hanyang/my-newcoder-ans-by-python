for _ in range(int(input())):
    n,p=map(int,input().split())
    print('Circus Act',_+1,end='')
    print(':')
    if n*0.5*5<=p or n==1:
        print('Chester can do it!')
        print()
    else:
        print('Chester will fail!')
        print()
