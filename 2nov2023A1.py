#finding minimum value from the list
n=int(input())
l=list(map(int,input().split()))
min=l[-1]
for i in l:
    if i<min:
        min=i
print(min)
