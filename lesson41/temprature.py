from tkinter import *
def f_to_c():
    far=ent_temp.get()
    cel=(5/9)*(float(far)-32)
    la1["text"]=f"{round(cel,2)}\N{DEGREE CELSIUS}"
    
    
root=Tk()
root.title("temperature converter")
root.geometry("400x400")
frame=Frame(master=root)
ent_temp=Entry(master=frame,width=10)
lb2=Label(master=frame,text="\N{DEGREE FAHRENHEIT}")
ent_temp.grid(row=0,column=0,sticky="e")
lb2.grid(row=0,column=1,sticky="w")
btn=Button(master=root,text="convert",command=f_to_c)
la1=Label(master=root,text="\N{DEGREE CELSIUS}")
frame.grid(row=0,column=0,padx=10)
btn.grid(row=0,column=1,pady=10)
la1.grid(row=0,column=2,padx=10)
root.mainloop()