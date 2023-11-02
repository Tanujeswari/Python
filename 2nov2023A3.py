#Wap to find the Second min from using function
def minlist(l):
    min=l[0]
    for i in l:
        if i<min:
            min=i
    return min
n=int(input())
l=list(map(int,input().split()))
fmin=minlist(l)
l.remove(fmin)
smin=minlist(l)
print(smin)
