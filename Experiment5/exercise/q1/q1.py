from tkinter import *

''' Filehandling part'''
def save_info():
    firstname_info = firstname.get()
    feedback_info = feedback.get()
    
    print(firstname_info,feedback_info )
    
    file = open("ques1.txt","w")
    
    file.write("Your First Name:" + firstname_info)
    
    file.write("\n")
    
    file.write("Feedback:" + feedback_info )
  
    file.close()

    
'''
Tkinter part
'''

app = Tk()

app.geometry("500x400")

app.title("Python File Handling in Forms")

heading = Label(text="Python File Handling in Forms",fg="black",width="500",height="3",font="10")

heading.pack()

firstname_text = Label(text="FirstName :")
feedback_text = Label(text="Feedback :")


firstname_text.place(x=215,y=70)
feedback_text.place(x=215,y=140)


firstname = StringVar()
feedback = StringVar()


first_name_entry = Entry(textvariable=firstname,width="30",justify='center')
feedback_entry = Entry(textvariable=feedback,width="30")

first_name_entry.place(x=143,y=100)
feedback_entry.place(x=143,y=180)


button = Button(app,text="Submit Data",command=save_info,width="30",height="2",bg="yellow")

button.place(x=0,y=50)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

mainloop()
