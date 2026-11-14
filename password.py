from tkinter import *


win=Tk()
win.title ("Password Strength Checker")
win.geometry("450x560")


def check_strength():
    password= entry.get()
    length = len(password)



    if length < 5:
        result.config(text="Weak password", fg="cyan")
    elif length < 8:
        result.config(text = "medium password", fg = "red")
    else:
        result.config(text="strong password", fg = "green")



Label(win, text="enter your passord").pack(pady=10)


entry = Entry(win, show="*")
entry.pack(pady=10)


Button(win, text="Check Strength", command= check_strength).pack(pady=10)


result = Label(win,text="")
result.pack(pady=10)

win.mainloop()


