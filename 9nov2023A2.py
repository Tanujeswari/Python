#print the prime number count
m=int(input())
c=0
for n in range(1,m):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        c=c+1
print(c)
