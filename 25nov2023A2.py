n=int(input())
A=[]
for i in range(n):
    l=list(map(int,input().split()))
    A.append(l)
for i in range(0,n):
    maxx=A[i][0]
    for j in range(0,n):
        if A[j][i]>maxx:
            maxx=A[j][i]
    print(maxx,end=' ')
