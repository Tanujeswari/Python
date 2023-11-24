def mysub():
    a=int(num1.get())
    b=int(num2.get())
    s=a-b
    res="Result:"+str(s)
    l3.config(text=s)
from tkinter import *
subtract=Tk()
subtract.title("Subtracting 2 numbers")
l1=Label(subtract,text="Enter First Number")
num1=Entry(subtract)
l2=Label(subtract,text="Enter Second Number")
num2=Entry(subtract)
b=Button(subtract,text="Sub",command=mysub)
l3=Label(subtract,text="?")
l1.grid(row=0,column=0)
num1.grid(row=0,column=1)
l2.grid(row=1,column=0)
num2.grid(row=1,column=1)
b.grid(row=2,column=0)
l3.grid(row=2,column=1)
subtract.mainloop()


