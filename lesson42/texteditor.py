from tkinter import *
from tkinter.filedialog import askopenfilename , asksaveasfilename
root=Tk()
root.title("text editor")
root.geometry("600x500")
root.rowconfigure(0,minsize=800,weight=1)
root.columnconfigure(1,minsize=800,weight=1)
def openfile():
    filepath=askopenfilename(filetypes=[("text files","*.txt"),("all files","*.*")])
    if not filepath:
        return text_edit.delete(1.0,END)
    with open (filepath,"r") as input_file:
        text=input_file.read()
        text_edit.insert(END,text)
        input_file.close()
    root.title(f"text editor - {filepath}")
def save_file():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[("text files","*.txt"),("all files","*.*")])
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text=text_edit.get(1.0,END)
        output_file.write(text)
    root.title(f"text editor - {filepath}")
text_edit=Text(root)
fr_button=Frame(root,relief=RAISED,bd=2)
btn_open=Button(fr_button,text="open",command=openfile)
btn_save=Button(fr_button,text="save as..",command=save_file)
btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)
fr_button.grid(row=0,column=0,sticky="ns")
text_edit.grid(row=0,column=1,sticky="nsew")
root.mainloop()