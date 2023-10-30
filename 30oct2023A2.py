def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
        i=i+1
    if s==n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
t=int(input())
for i in range(t):
    n=int(input())
    perfect(n)
