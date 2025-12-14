import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("HESSAP MAKİNESİ")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky="NWES")

root.mainloop()
