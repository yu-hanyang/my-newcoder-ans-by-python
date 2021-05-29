n=int(input())
out=2*(n//4)
n_y=n%4
if n_y==3:
    out+=1
else:out+=n_y
print(out)
