amount=int(input())
tt=0
fh=0
th=0
oh=0
ft=0
twenty=0
ten=0
five=0
two=0
one=0
while(amount>=2000):
    tt=tt+1
    amount=amount-2000
while(amount>=500):
    fh=fh+1
    amount=amount-500
while(amount>=200):
    th=th+1
    amount=amount-200
while(amount>=100):
    oh=oh+1
    amount=amount-100
while(amount>=50):
    ft=ft+1
    amount=amount-50
while(amount>=20):
    twenty=twenty+1
    amount=amount-20
while(amount>=10):
    ten=ten+1
    amount=amount-10
while(amount>=5):
    five=five+1
    amount=amount-5
while(amount>=2):
    two=two+1
    amount=amount-2
while(amount>=1):
    one=one+1
    amount=amount-1
if tt>0:
    print('2000:'+str(tt))
if fh>0:
    print('500:'+str(fh))
if th>0:
    print('200:'+str(th))
if oh>0:
    print('100:'+str(oh))
if ft>0:
    print('50:'+str(ft))
if twenty>0:
    print('20:'+str(twenty))
if ten>0:
    print('10:'+str(ten))
if five>0:
    print('5:'+str(five))
if two>0:
    print('2:'+str(two))
if one>0:
    print('1:'+str(one))
