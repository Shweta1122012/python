from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("virus detected")
root.geometry("400x400")
def messege():
    messagebox.showwarning("alert","virus detected")

btn=Button(root,text="scan for virus",command=messege)
btn.place(x=100,y=120)
root.mainloop()