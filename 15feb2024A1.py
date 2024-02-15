sname=input('Enter the student name:')
s1=int(input('Enter first subject marks:'))
s2=int(input('Enter second subject marks:'))
s3=int(input('Enter third subject marks:'))
total=s1+s2+s3
avg=total//3
if avg>85 and avg<100:
    print('First')
elif avg>75 and avg<85:
    print('Second')
elif avg>65 and avg<75:
    print('Third')
elif avg>55 and avg<65:
    print('Fourth')
elif avg>45 and avg<55:
    print('Five')
else:
    print('Fail')
    
