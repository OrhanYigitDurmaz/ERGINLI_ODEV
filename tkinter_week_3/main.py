import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x800")
root.title("HESAP MAKİNESİ")
# windows calculatorun normali 3:2

content = ttk.Frame(root)
namelbl = ttk.Label(content, text="0", style="W.TLabel", anchor="e")

# style kısmını geeksforgeeks sitesinden baktım
# https://tkdocs.com/tutorial/styles.html
#
#
# This will create style object
lblstyle = ttk.Style()
btnstyle = ttk.Style()

# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).
#
# (method) def configure(
#    style: str,
#    query_opt: None = None,
#    **kw: Any
# ) -> None
#
#
# https://tkdocs.com/tutorial/customstyles.html#:~:text=background%3D%5B%28%27disabled%27%2C%27%23d9d9d9%27%29%2C%20%28%27active%27%2C%27%23ececec%27%29%5D%2C
lblstyle.configure(
    "W.TLabel",
    font=("calibri", 30, "bold"),
)

btnstyle.configure(
    "TButton",
    font=("calibri", 20, "bold"),
)


one = ttk.Button(content, text="1")
two = ttk.Button(content, text="2")
three = ttk.Button(content, text="3")
four = ttk.Button(content, text="4")
five = ttk.Button(content, text="5")
six = ttk.Button(content, text="6")
seven = ttk.Button(content, text="7")
eight = ttk.Button(content, text="8")
nine = ttk.Button(content, text="9")
zero = ttk.Button(content, text="0")

plusnegative = ttk.Button(content, text="⁺/₋")  # (U+207A) + / + (U+208B)
dotbutton = ttk.Button(content, text=".")
equal = ttk.Button(content, text="=")
plus = ttk.Button(content, text="+")
negative = ttk.Button(content, text="-")
times = ttk.Button(content, text="x")
divide = ttk.Button(content, text="÷")
delete = ttk.Button(content, text="⌫")  # (U+232B)
cbutton = ttk.Button(content, text="C")
cebutton = ttk.Button(content, text="CE")
percent = ttk.Button(content, text="%")
square = ttk.Button(content, text="x²")  # x + (U+00B2)
rootof = ttk.Button(content, text="²√x")  # (U+00B2) + (U+221A) + x
reciprocal = ttk.Button(content, text="¹/ₓ")  # (U+00B9) + / + (U+2093)

content.grid(column=0, row=0, sticky="nsew")
namelbl.grid(column=0, row=0, columnspan=4, sticky="nsew")
one.grid(column=0, row=5, sticky="nsew")
two.grid(column=1, row=5, sticky="nsew")
three.grid(column=2, row=5, sticky="nsew")

four.grid(column=0, row=4, sticky="nsew")
five.grid(column=1, row=4, sticky="nsew")
six.grid(column=2, row=4, sticky="nsew")

seven.grid(column=0, row=3, sticky="nsew")
eight.grid(column=1, row=3, sticky="nsew")
nine.grid(column=2, row=3, sticky="nsew")

zero.grid(column=1, row=6, sticky="nsew")

plusnegative.grid(column=0, row=6, sticky="nsew")
dotbutton.grid(column=2, row=6, sticky="nsew")
equal.grid(column=3, row=6, sticky="nsew")
plus.grid(column=3, row=5, sticky="nsew")
negative.grid(column=3, row=4, sticky="nsew")
times.grid(column=3, row=3, sticky="nsew")
divide.grid(column=3, row=2, sticky="nsew")
delete.grid(column=3, row=1, sticky="nsew")
cbutton.grid(column=2, row=1, sticky="nsew")
cebutton.grid(column=1, row=1, sticky="nsew")
percent.grid(column=0, row=1, sticky="nsew")
square.grid(column=1, row=2, sticky="nsew")
rootof.grid(column=2, row=2, sticky="nsew")
reciprocal.grid(column=0, row=2, sticky="nsew")


# content.columnconfigure(0, weight=1)
# content.columnconfigure(1, weight=1)
# content.columnconfigure(2, weight=1)
# content.columnconfigure(3, weight=1)
for i in range(0, 4):
    content.columnconfigure(i, weight=1)

# content.rowconfigure(0, weight=1)
# content.rowconfigure(1, weight=1)
# content.rowconfigure(2, weight=1)
# content.rowconfigure(3, weight=1)
# content.rowconfigure(4, weight=1)
# content.rowconfigure(5, weight=1)
# content.rowconfigure(6, weight=1)

for i in range(0, 7):
    content.rowconfigure(i, weight=1)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
