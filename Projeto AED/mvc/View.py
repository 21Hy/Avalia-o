import tkinter as tk
from model.User import*
from model.LinkedList import*
from Controller import*
from model.Despesas import*

class View:
    def __init__(self,master):
        self.master = master
        self.despesas = LinkedList()
        self.controller = Controller(self.master)
        self.lista_de_objetos_despesas = []
        self.criar_login()

    def modificar_geometria(self):
        # geometria centrada da janela
        w=300; h=300
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width/2)-(w/2)
        y = (screen_height/2)-(h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def criar_login(self):
        self.modificar_geometria()
        self.main_label = tk.Label(self.master, text='Login', font='bold', pady=20)
        # username frame
        self.un_fr = tk.Frame(self.master)
        self.un_lb = tk.Label(self.un_fr, text='Username') 
        self.un_et_str = tk.StringVar()
        self.un_et = tk.Entry(self.un_fr, width=30, textvariable=self.un_et_str, bg='#b2bdd9') # hex color picker
        # password frame
        self.pw_fr = tk.Frame(self.master, pady=10)
        self.pw_lb = tk.Label(self.pw_fr, text='Password') 
        self.pw_et_str = tk.StringVar()
        self.pw_et = tk.Entry(self.pw_fr, width=30,textvariable=self.pw_et_str, show='*', bg='#b2bdd9')
        # nif frame
        self.nif_fr = tk.Frame(self.master, pady=10)
        self.nif_lb = tk.Label(self.pw_fr, text='Nif') 
        self.nif_et_str = tk.StringVar()
        self.nif_et = tk.Entry(self.pw_fr, width=30,textvariable= self.nif_et_str, bg='#b2bdd9') 
        # Entry frame
        self.et_frame = tk.Frame(self.master)
        self.et_bt_in = tk.Button(self.et_frame, text="Enter", width=25, bg='#c4c2bc')
        self.et_bt_in.config(command= lambda: self.controller.login_enter_click(self.un_et_str,self.pw_et_str,self.nif_et_str))
        self.et_lb = tk.Label(self.et_frame)
        self.et_bt_sp = tk.Button(self.et_frame, text="Don´t have an acount yet? Sign up here", font=('','7'), bg='#c4c2bc',width=29)
        self.et_bt_sp.config(command = self.sign_up_window)
        # packs
        self.main_label.pack()
        self.un_fr.pack()
        self.un_lb.pack()
        self.un_et.pack()
        self.pw_fr.pack()
        self.pw_lb.pack()
        self.pw_et.pack()
        self.nif_fr.pack()
        self.nif_lb.pack()
        self.nif_et.pack()
        self.et_frame.pack()
        self.et_bt_in.pack()
        self.et_lb.pack()
        self.et_bt_sp.pack()

    def sign_up_window(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.modificar_geometria()
        self.main_label_2 = tk.Label(self.master, text='Sign-up', font='bold', pady=20)
        # username frame
        self.un_fr = tk.Frame(self.master)
        self.un_lb = tk.Label(self.un_fr, text='Username') 
        self.un_et_str = tk.StringVar()
        self.un_et = tk.Entry(self.un_fr, width=30, textvariable=self.un_et_str, bg='#b2bdd9') # hex color picker
        # password frame
        self.pw_fr = tk.Frame(self.master, pady=10)
        self.pw_lb = tk.Label(self.pw_fr, text='Password') 
        self.pw_et_str = tk.StringVar()
        self.pw_et = tk.Entry(self.pw_fr, width=30,textvariable=self.pw_et_str, show='*', bg='#b2bdd9')
        # password frame
        self.pw_lb_2 = tk.Label(self.pw_fr, text='Confirm password') 
        self.pw_et_str_2 = tk.StringVar()
        self.pw_et_2 = tk.Entry(self.pw_fr, width=30,textvariable=self.pw_et_str_2, show='*', bg='#b2bdd9')
        # nif frame
        self.nif_lb_2 = tk.Label(self.pw_fr, text='Nif') 
        self.nif_et_str_2 = tk.StringVar()
        self.nif_et_2 = tk.Entry(self.pw_fr, width=30,textvariable=self.nif_et_str_2, bg='#b2bdd9')
        # Entry frame
        self.et_fr = tk.Frame(self.master)
        self.et_bt_in = tk.Button(self.et_fr, text="Enter", width=25, bg='#c4c2bc')
        self.et_bt_in.config(command=lambda:self.controller.sign_up_click(self.un_et_str,self.pw_et_str, self.pw_et_str_2, self.nif_et_str_2))
        # packs
        self.main_label_2.pack()
        self.un_fr.pack()
        self.un_lb.pack()
        self.un_et.pack()
        self.pw_fr.pack()
        self.pw_lb.pack()
        self.pw_et.pack()
        self.pw_lb_2.pack()
        self.pw_et_2.pack()
        self.nif_lb_2.pack()
        self.nif_et_2.pack()
        self.et_fr.pack()
        self.et_bt_in.pack()
        # end-loop
        self.master.mainloop()

    indice_de_despesa = 0
    def inserir_despesa_linkedlist(self, categoria, descricao, valor, data):
        self.despesas.insert(
            Despesas(categoria.get(),descricao.get(),valor.get(),data.get()),
            View.indice_de_despesa)
        View.indice_de_despesa +=1

    def guardar_linkedlist(self):
        for i in range(View.indice_de_despesa + 1):
            self.lista_de_objetos_despesas.append(self.despesas.get(i))

        for elemento in self.lista_de_objetos_despesas:
            self.controller.user_data.append(
                {
                    'Categoria': elemento.get_categoria(),
                    'Descrição': elemento.get_descricao(),
                    'Valor': elemento.get_valor(),
                    'Data': elemento.get_data()
                }
            )
    def ordenar_despesas_periodo_tempo(self):
        pass

    def ordenar_despesas_categoria(self, categoria):
        self.lista_de_objetos_despesas_ordenados = []
        for elemento in self.lista_de_objetos_despesas:
            if elemento.get_categoria() == categoria:
                self.lista_de_objetos_despesas_ordenados.append(elemento)
                
    def ordenar_despesas_valor_crescente(self):
        pass
    def ordenar_despesas_valor_decrescente(self):
        pass
    def ordem_despesas_ordem_alfabética(self):
        pass
