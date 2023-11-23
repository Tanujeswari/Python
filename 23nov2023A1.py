def prime(n):
    i=1
    c=0
    while i<=n:
        if n%i==0:
            c=c+1
        i=i+1
    if c==2:
        return True
    else:
        return False

n=int(input())
l=[i for i in range(1,n+1) if prime(i)]
for i in l:
    print(i,end=' ')
