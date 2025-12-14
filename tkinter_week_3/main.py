import tkinter as tk
from tkinter import ttk

root = tk.Tk()

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=200)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

one = ttk.Button(content, text="One")
two = ttk.Button(content, text="Two")
three = ttk.Button(content, text="Three")
four = ttk.Button(content, text="Four")
five = ttk.Button(content, text="Five")
six = ttk.Button(content, text="Six")
seven = ttk.Button(content, text="Seven")
eight = ttk.Button(content, text="Eight")
nine = ttk.Button(content, text="Nine")
zero = ttk.Button(content, text="Zero")


content.grid(column=0, row=0, sticky="nsew")
frame.grid(column=0, row=0, columnspan=3, rowspan=2)
# namelbl.grid(column=3, row=0, columnspan=2)
# name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=4)
two.grid(column=1, row=4)
three.grid(column=2, row=4)

four.grid(column=0, row=3)
five.grid(column=1, row=3)
six.grid(column=2, row=3)

seven.grid(column=0, row=2)
eight.grid(column=1, row=2)
nine.grid(column=2, row=2)

zero.grid(column=2, row=5)


content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.columnconfigure(3, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)
content.rowconfigure(3, weight=1)
content.rowconfigure(4, weight=1)
content.rowconfigure(5, weight=1)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
