import tkinter as tk
from tkinter import ttk


class Ver():
    def __init__(self):
        self.gestor_despesas()
        
    def modificar_geometria(self, largura, altura):
        # geometria centrada da janela
        w=largura; h=altura
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width/2)-(w/2)
        y = (screen_height/2)-(h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def gestor_despesas(self):
        self.master = tk.Tk()
        self.master.resizable(False,False)
        self.modificar_geometria(800,500)
        self.frame1 = tk.Frame(self.master, bg='pink')
        self.frame2 = tk.Frame(self.master, bg='yellow')
        self.frame2_lb1 = tk.Label(self.frame2, text='Adicionar Despesas',font=('Arial', 20))
        self.frame2_lb2 = tk.Label(self.frame2, text='Categoria:',font=('Arial', 14))
        self.frame2_lb3 = tk.Label(self.frame2, text='Valor(€):',font=('Arial', 14))
        self.frame2_lb4 = tk.Label(self.frame2, text='Data:',font=('Arial', 14))
        self.frame2_lb5 = tk.Label(self.frame2, text='Descrição: ',font=('Arial', 14))
        self.frame2_cb1_lista =['Alimentação', 'Outros']
        self.frame2_cb1 = ttk.Combobox(self.frame2,font=('Arial', 14), values=self.frame2_cb1_lista)
        self.frame1_et = tk.Entry(self.frame1,font=('Arial', 14))
        self.frame2_et = tk.Entry(self.frame2, font=('Arial', 14) )
        self.frame2_et2 = tk.Entry(self.frame2,font=('Arial', 14))
        self.frame2_text = tk.Text(self.frame2,font=('Arial', 14), width=20, height=3)
        self.frame2_bt= tk.Button(self.frame2, text= 'Enter')
        self.frame3 = tk.Frame(self.frame2, bg= 'light blue', width=200, height=100)
        self.frame3_lb = tk.Label(self.frame3,text='Limite mensal:',font=('Arial', 10))
        self.frame3_et = tk.Entry(self.frame3,font=('Arial', 10))
        self.frame3_bt = tk.Button(self.frame3, font=('Arial', 10), text='Enter')
        self.gestor_despesas_grids()
        self.master.mainloop()

    def gestor_despesas_grids(self):
        # definição da grid
        # culunas:
        self.master.columnconfigure(0,weight= 1,uniform='a')
        self.master.columnconfigure(1,weight= 1,uniform='a')
        self.master.columnconfigure(2,weight= 1,uniform='a')
        self.master.columnconfigure(3,weight= 1,uniform='a')
        self.master.columnconfigure(4,weight= 1,uniform='a')
        self.master.columnconfigure(5,weight= 1,uniform='a')
        # linhas:
        self.master.rowconfigure(0,weight=1,uniform='a')
        self.master.rowconfigure(1,weight=1,uniform='a')
        self.master.rowconfigure(2,weight=1,uniform='a')
        self.master.rowconfigure(3,weight=1,uniform='a')
        self.master.rowconfigure(4,weight=1,uniform='a')
        self.master.rowconfigure(5,weight=1,uniform='a')
        # objetos na grid:
        self.frame1.grid(row=0,column=0,rowspan=4,columnspan=6,sticky='nswe')
        self.frame2.grid(row=0,column=6,rowspan=4,columnspan=2,sticky='nswe')
        
    

        # frame2
        self.frame2_lb1.pack(ipadx=5,ipady=5, pady=10)
        self.frame2_lb2.pack()
        self.frame2_cb1.pack()
        self.frame2_lb3.pack()
        self.frame2_et.pack()
        self.frame2_lb4.pack()
        self.frame2_et2.pack()
        self.frame2_lb5.pack()
        self.frame2_text.pack()
        self.frame2_bt.pack(pady=5, ipadx=90, ipady=5)
        self.frame3.pack()
        self.frame3_lb.pack(side='left')
        self.frame3_bt.pack(side='right')
        self.frame3_et.pack(ipady=5)

Ver()
