n=int(input())
l=list(map(int,input().split()))
n=[]
p=[]
for i in l:
    if i%2==0:
        p.append(i)
    else:
        n.append(i)
res=p+n
for i in res:
    print(i,end=' ')
