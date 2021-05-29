for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    if a<350:
        print('You have not enough minerals.')
    elif b<250:
        print('You require more vespene gas.')
    elif x+6>y:
        print('You must construct additional pylons.')
    else:
        print('Carrier has arrived.')