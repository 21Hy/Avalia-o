import tkinter as tk
from Controller import * 

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.controller = Controller(self.root)
        self.root.mainloop()



