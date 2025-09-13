from tkinter import *
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    dob_str = dob_entry.get()
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter date in YYYY-MM-DD format.")

root = Tk()
root.title("Age Calculator")
Label(root, text="Enter your Date of Birth (YYYY-MM-DD):").pack(pady=10)
dob_entry = Entry(root)
dob_entry.pack(pady=5)

Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)
result_label = Label(root, text="")
result_label.pack(pady=10)
def calculate_exact_age(dob, today):
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days_in_prev_month = (datetime(prev_year, prev_month + 1, 1) - datetime(prev_year, prev_month, 1)).days
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def calculate_age():
    dob_str = dob_entry.get()
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = datetime.today()
        years, months, days = calculate_exact_age(dob, today)
        result_label.config(text=f"Your age is:"+years+" years, "+months+" months, and "+days+" days")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter date in YYYY-MM-DD format.")
root.mainloop()