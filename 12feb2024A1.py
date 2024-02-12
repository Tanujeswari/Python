n=int(input("Enter n value:"))
temp=n
res=0
while n!=0:
    r=n%10
    n=n//10
    res=res+r*r*r
print(res)
if temp==res:
    print("Armstrong")
else:
    print("Not Armstrong")
