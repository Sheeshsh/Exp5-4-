from tkinter import *
import sqlite3

def reg():
 
 c.execute('insert into sdetails values(?,?,?,?)',(num1.get(),num2.get(),num3.get(),num4.get()))
 conn.commit()
 
def sear():
 res=c.execute('select * from sdetails where Sno=?',(self.num1.get(),))
 num2.delete(0,END)
 num3.delete(0,END)
 num4.delete(0,END)
 for r in res.fetchall():
     num2.insert(0,r[1])
     num3.insert(0,r[2])
     num4.insert(0,r[3])
 


conn=sqlite3.connect('student.db')
c=conn.cursor() 
master=Tk()
master.geometry("300x200")
l1=Label(master,text="Sno")
l2=Label(master,text="Name")
l3=Label(master,text="Age")
l4=Label(master,text="Qualification")
 
num1=Entry(master)
num2=Entry(master)
num3=Entry(master)
num4=Entry(master)
 
l1.place(x=10,y=20)
num1.place(x=100,y=20)
l2.place(x=10,y=50)
num2.place(x=100,y=50)
l3.place(x=10,y=90)
num3.place(x=100,y=90)
l4.place(x=10,y=130)
num4.place(x=100,y=130)
 
b1=Button(master,text="Register",command=reg)
b1.place(x=40,y=170)
b2=Button(master,text="Quit",command=master.destroy)
b2.place(x=100,y=170)
b3=Button(master,text="Search",command=sear)
b3.place(x=160,y=170)
  

master.mainloop()
