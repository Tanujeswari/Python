def mysem():
    sem1=int(sem1points.get())
    sem2=int(sem2points.get())
    sem3=int(sem3points.get())
    sem4=int(sem4points.get())
    sem5=int(sem5points.get())
    sem6=int(sem6points.get())
    total=sem1+sem2+sem3+sem4+sem5+sem6
    avg=total//6
    if avg==10:
        gp="O"
    elif avg>=9:
        gp="A+"
    elif avg>=8:
        gp="A"
    elif avg>=7:
        gp="B"
    elif avg>=6:
        gp="C"
    elif avg>=5:
        gp="D"
    elif avg>=4:
        gp="P"
    else:
        gp="F"
    s="CGPA:"+str(avg)+" Result:"+gp
    res.config(text=s)
from tkinter import *
result=Tk()
result.title("Student Result")
sem1=Label(result,text="Enter Sem 1 Points:")
sem1points=Entry(result)
sem2=Label(result,text="Enter Sem 2 Points:")
sem2points=Entry(result)
sem3=Label(result,text="Enter Sem 3 Points:")
sem3points=Entry(result)
sem4=Label(result,text="Enter Sem 4 Points:")
sem4points=Entry(result)
sem5=Label(result,text="Enter Sem 5 Points:")
sem5points=Entry(result)
sem6=Label(result,text="Enter Sem 6 Points:")
sem6points=Entry(result)
b1=Button(result,text="Submit",command=mysem)
res=Label(result,text="?")
sem1.grid(row=0,column=0)
sem1points.grid(row=0,column=1)
sem2.grid(row=1,column=0)
sem2points.grid(row=1,column=1)
sem3.grid(row=2,column=0)
sem3points.grid(row=2,column=1)
sem4.grid(row=3,column=0)
sem4points.grid(row=3,column=1)
sem5.grid(row=4,column=0)
sem5points.grid(row=4,column=1)
sem6.grid(row=5,column=0)
sem6points.grid(row=5,column=1)
b1.grid(row=6,column=0)
res.grid(row=6,column=1)
result.mainloop()
