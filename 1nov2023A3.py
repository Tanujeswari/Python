n=int(input())
l=[]
for i in range(1,n+1,1):
    a=int(input())
    l.append(a)
print(max(l)-min(l))
