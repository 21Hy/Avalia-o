import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x300')
root.columnconfigure(1,weight=1)
root.rowconfigure(1,weight=1)




frame_label = ttk.LabelFrame(
    text="Filtros", padding=(20, 10)
)
frame_label.grid(
        row=0, column=0, padx=(10, 10), pady=(20, 10), sticky="nsew"
)
frame_label2 = ttk.LabelFrame(
    text="Mais Filtros", padding=(20, 10)
)
frame_label2.grid(
        row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
)
# Radiobuttons

# 1
radio_1 = ttk.Radiobutton(
    frame_label, text="Valor decrescente", value=1
)
radio_1.grid(row=0, column=0, padx=3, pady=5, sticky="nsew")
# 2
radio_2 = ttk.Radiobutton(
    frame_label, text="Valor crescente", value=1
)
radio_2.grid(row=1, column=0, padx=3, pady=5, sticky="nsew")

# 3
radio_3 = ttk.Radiobutton(
    frame_label, text="Alfabéticamente", value=1
)
radio_3.grid(row=2, column=0, padx=3, pady=5, sticky="nsew")

# 4
bt = ttk.Button(
    frame_label, text='Enter'
)
bt.grid(row=3, column=0, padx=3, pady=5, sticky="nsew")

#####
label1 = ttk.Label(frame_label2, text='Por Categoria:')
label1.grid(row=0, column=0, padx=3, pady=0, sticky="nsew")
entry1 = ttk.Entry(frame_label2)
entry1.grid(row=1, column=0, padx=3, pady=5, sticky="nsew")

label2 = ttk.Label(frame_label2, text='Por Data:')
label2.grid(row=2, column=0, padx=3, pady=0, sticky="nsew")
entry2 = ttk.Entry(frame_label2)
entry2.grid(row=3, column=0, padx=3, pady=5, sticky="nsew")

bt2 = ttk.Button(
    frame_label2, text='Enter'
)
bt2.grid(row=4, column=0, padx=3, pady=5, sticky="nsew")

root.mainloop()


