s,e=map(int,input().split())
i=len(str(e))
for temp in range(s,e+1):
    n=temp
    res=0
    while n!= 0:
        r=n%10
        n=n//10
        res=res+r*r*r
    if temp==res:
        print(res,end=' ')
