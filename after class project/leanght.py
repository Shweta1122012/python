from tkinter import *
def i_to_c():
    inches = ent_temp.get()
    try:
        inches = float(inches)
        cen = inches * 2.54
        la1["text"] = f"{round(cen, 2)} centimetres"
    except ValueError:
        la1["text"] = "Invalid input"
    
    
root=Tk()
root.title("length converter")
root.geometry("400x400")
frame=Frame(master=root)
ent_temp=Entry(master=frame,width=10)
lb2=Label(master=frame,text="centimetres")
ent_temp.grid(row=0,column=0,sticky="e")
lb2.grid(row=0,column=1,sticky="w")
btn=Button(master=root,text="convert",command=i_to_c)
la1=Label(master=root,text="inches")
frame.grid(row=0,column=0,padx=10)
btn.grid(row=0,column=1,pady=10)
la1.grid(row=0,column=2,padx=10)
root.mainloop()