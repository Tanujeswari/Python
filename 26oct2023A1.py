n=int(input("Enter n value:"))
temp=n
res=0
while n!=0:
    r=n%10
    n=n//10
    res=res*10+r
print(res)
if temp==res:
    print("Palindrome")
else:
    print("Not palindrome")
