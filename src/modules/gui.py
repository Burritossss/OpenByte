from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        ttk.Label(self.frm, text="Test").grid(column=0, row=0)


gui = GUI()

gui.root.mainloop()