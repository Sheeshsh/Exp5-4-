from tkinter import *
import sqlite3
from tkinter import messagebox

def Submit():
    c.execute('insert into form values(?,?)',(e1.get(),e2.get()))
    conn.commit()
    
def signin():
     c.execute('select * from form  ')
     r = c.fetchall()
     count=1
     for i in r:
        if(i[0]==e1.get() and i[1]==int(e2.get())):
           count=1
           break
        else:
            count=0
     if(count==1):
         messagebox.showinfo("Welcome", "Login Successful")
         messagebox.showinfo("Welcome","WELCOME TO PYTHON")
     elif(count==0):
         messagebox.showinfo("Sorry", "Invalid Username and Password")


conn=sqlite3.connect("G:/Programming Series 2022/Python Experiments/Experiment5/exercise/q2/form.db")
c=conn.cursor()
root=Tk()
root.geometry("300x200")
Name=Label(root,text="Username*")
Name.grid(row=0,column=0,pady=10)
Password=Label(root,text="Password*")
Password.grid(row=1,column=0,pady=10)
Button1=Button(root,text="Register",command=Submit)
Button1.grid(row=2,column=0,padx=20,pady=20)
Button2=Button(root,text="Quit",command=root.destroy)
Button2.grid(row=2,column=1,pady=20)
Button3=Button(root,text="Sign in",command=signin)
Button3.place(x=88,y=100)

e1=Entry(root)
e1.grid(row=0,column=1)

e2=Entry(root,show='')
e2.grid(row=1,column=1)
root.mainloop()
