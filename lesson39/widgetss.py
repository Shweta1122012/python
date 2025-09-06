from tkinter import *
from datetime import date
root=Tk()
root.title("welcome to widgets")
root.geometry("400x300")
lb1=Label(text="hello",fg="white",bg="blue",height=1,width=300)
namelb=Label(text="full name",bg="blue")
nameentry=Entry()
def display():
    name=nameentry.get()
    global Message
    message="welcome to the application \n todays date is: "
    greet="hello " +name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="begin",command=display , height=1,width=20,bg="blue",fg="white")
lb1.pack()
namelb.pack()
nameentry.pack()
btn.pack()
text_box.pack()

root.mainloop()