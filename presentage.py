
from tkinter import *
from datetime import date

window = Tk()
window.title("Age Calculator")
window.geometry("300x350")

Label(window, text="Birth Day").pack()
d = Entry(window)
d.pack()

Label(window, text="Birth Month").pack()
m = Entry(window)
m.pack()

Label(window, text="Birth Year").pack()
y = Entry(window)
y.pack()

def age():
    b = date(int(y.get()), int(m.get()), int(d.get()))
    Label(window, text=f"Present Age: {date.today().year - b.year}").pack()

Button(window, text="Calculate Age", command=age).pack()

window.mainloop()
