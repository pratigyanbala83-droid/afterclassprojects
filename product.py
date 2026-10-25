

from tkinter import *

window = Tk()
window.title("Product")
window.geometry("560x400")

Label(window, text="Enter first number").pack()
num1 = Entry(window)
num1.pack()

Label(window, text="Enter second number").pack()
num2 = Entry(window)
num2.pack()

box = Text(window, height=2, width=30)
box.pack()

def dis():
    a = float(num1.get())
    b = float(num2.get())
    product = a * b

    box.delete("1.0", END)
    box.insert(END, "Product = " + str(product))

Button(window, text="Multiply", command=dis).pack()

window.mainloop()
