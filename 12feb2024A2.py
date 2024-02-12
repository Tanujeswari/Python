class Armstrong:
    def check(self,n):
        count=0
        first=n
        while first>0:
            num=first %10
            count += num**3
            first //=10
        if (n==count):
            print(n,"is a armstrong")
        else:
            print(n,"is not armstrong")
arm=Armstrong()
n=int(input())
arm.check(n)
