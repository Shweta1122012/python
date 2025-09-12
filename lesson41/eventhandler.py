from tkinter import *
window=Tk()
window.title("event handler")
window.geometry("400x400")
def key_pressed(event):
    '''print the associate key of the pressed key'''
    print(event.char)
window.bind("<Key>",key_pressed)

def button_clicked(event):
    print("button clicked")
btn=Button(text="click me!")
btn.pack()
btn.bind("<Button-1>",button_clicked)
window.mainloop()