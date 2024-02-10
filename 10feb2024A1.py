n=int(input())
s=list(map(int,input().split()))
d={}
for k in s:
    if k not in d:
        d[k]=1
    else:
        d[k]=d[k]+1
for k in d:
    if d[k]>1:
        print(k,end=' ')
