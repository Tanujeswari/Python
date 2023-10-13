shirt=2
pant=300
hat=400
print('******Welcome to bts******')
cname=input('Enter customer name:')
cphno=input('Enter Phno:')
shirtq=int(input('Enter no of shirts:'))
pantq=int(input('Enter no of pants:'))
hatq=int(input('Enter no of hats:'))
pc=input('Enter promo code:')
bill=(shirt*shirtq)+(pant*pantq)+(hat*hatq)
if pc=='HOLI' or pc=='holi':
    disc=bill*50/100
elif pc=='SUNDAY' or pc=='sunday':
    disc=bill*40/100
elif bill>=2000:
    disc=bill*20/100
elif bill>=1000:
    disc=bill*10/100
elif bill>=500:
    disc=bill*5/100
else:
     disc=bill*3/100
tbill=bill-disc
gst=tbill*12/100
obill=tbill+gst
print('customer name:',cname)
print('customer phno:',cphno)
print('bill:',bill)
print('Discount:',disc)
print('Gst 12%:',gst)
print('Bill to be paid:',obill)
print('**Thank you***')
