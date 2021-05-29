def dw(x):
    if x>=3000:
        return 'Legendary Grandmaster'
    elif x>=2400:
        return 'Grandmaster'
    elif x>=2100:
        return 'Master'
    elif x>=1900:
        return 'Candidate Master'
    elif x>=1600:
        return 'Expert'
    elif x>=1400:
        return 'Specialist'
    elif x>=1200:
        return 'Pupil'
    else:return 'Newbie'
for _ in range(int(input())):
    a,b=map(int,input().split())
    if dw(a)==dw(b):
        print('No')
    else:
        print(dw(a),'to',dw(b))