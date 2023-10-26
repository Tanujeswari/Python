a,b,c=map(int,input().split())
max1=a if a>b else b
max2=c
print(max1) if max1>max2 else print(max2)
