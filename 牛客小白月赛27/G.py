n=int(input())
s=input()
k=s.count('k')
ing=min(s.count('i'),s.count('n'),s.count('g'))
if k>ing:
    print(ing)
elif 2*k<ing:
    print(2*k)
else:
    print(k+ing-k)
