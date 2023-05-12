import tkinter as tk
from model.Cliente import*
from model.LinkedList import*
from Controller import*
from model.Despesas import*
from tkinter import messagebox
from model.Iterador import *

class View:
    def __init__(self,master):
        self.master = master
        self.master.resizable(False, False)
        self.clientes = LinkedList()
        self.despesas = LinkedList()
        self.controller = Controller(self.master)
        self.preencher_users()
        self.user_atual = None
        self.despesas.insert_last(Despesas('Alimentação', 'descrição', 0,0))
        self.login()

    def modificar_geometria(self, largura, altura):
        # geometria centrada da janela
        w=largura; h=altura
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width/2)-(w/2)
        y = (screen_height/2)-(h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def login(self):
        self.modificar_geometria(250,400)
        self.frame = tk.Frame(self.master)
        self.lb_login = tk.Label(self.frame, text='Login', font=('Arial', 20))
        # username 
        self.un_lb = tk.Label(self.frame, text='Username',font=('Arial', 14)) 
        self.un_et = tk.Entry(self.frame, font=('Arial', 14), bg='#b2bdd9') 
        # password 
        self.pw_lb = tk.Label(self.frame, text='Password',font=('Arial', 14)) 
        self.pw_et = tk.Entry(self.frame, font=('Arial', 14), show='*', bg='#b2bdd9')
        # nif 
        self.nif_lb = tk.Label(self.frame, text='Nif',font=('Arial', 14)) 
        self.nif_et = tk.Entry(self.frame, font=('Arial', 14), bg='#b2bdd9') 
        # botões
        self.bt_login = tk.Button(self.frame, text="Enter",font=('Arial', 14), bg='#c4c2bc')
        self.bt_login.config(command = self.verificar_login)
        self.bt_sign_up = tk.Button(self.frame, text="Sign-up", font=('Arial', 14), bg='#c4c2bc')
        self.bt_sign_up.config(command = self.sign_up)
        self.login_packs()

    def sign_up(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.master.resizable(False, False)
        self.modificar_geometria(250,400)
        self.frame = tk.Frame(self.master)
        self.lb_sign_up = tk.Label(self.frame, text='Sign-up', font=('Arial', 20))
        # username 
        self.un_lb = tk.Label(self.frame, text='Username',font=('Arial', 14)) 
        self.un_et = tk.Entry(self.frame, font=('Arial', 14),  bg='#b2bdd9') 
        # password 
        self.pw_lb = tk.Label(self.frame, text='Password',font=('Arial', 14)) 
        self.pw_et = tk.Entry(self.frame, font=('Arial', 14), show='*', bg='#b2bdd9')
        # confirm password
        self.pw_lb_2 = tk.Label(self.frame, text='Confirm password',font=('Arial', 14)) 
        self.pw_et_2 = tk.Entry(self.frame, font=('Arial', 14), show='*', bg='#b2bdd9')
        # nif 
        self.nif_lb = tk.Label(self.frame, text='Nif',font=('Arial', 14)) 
        self.nif_et = tk.Entry(self.frame, font=('Arial', 14), bg='#b2bdd9')
        # Botão
        self.bt = tk.Button(self.frame, text="Enter", font=('Arial', 14), bg='#c4c2bc')
        self.bt.config(command= self.verificar_registo)
        self.sign_up_packs()
        self.master.mainloop()

    def gestor_despesas(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.master.resizable(False, False)
        self.modificar_geometria(800,500)
        # ...
        # ...
        # ...
        # ...
        # ...
        self.master.mainloop()

    def verificar_login(self):
        if (
            (self.clientes.find_nif(self.nif_et.get()) !=-1) and
            (self.clientes.get(
                    (self.clientes.find_nif(self.nif_et.get()))
                ).get_username() == self.un_et.get()) and
            (self.clientes.get(
                    (self.clientes.find_nif(self.nif_et.get()))
                ).get_password() == self.pw_et.get())
        ):
            self.user_atual = self.nif_et.get()
            self.preencher_despesas()
            self.guardar()
            self.gestor_despesas()
        else:
            self.produzir_msg_erro('Login', 'Falha no login', 0)

    def verificar_registo(self):
        if ( 
            (self.clientes.find_nif(self.nif_et.get()) != -1) or
            (self.pw_et.get() != self.pw_et_2.get()) or
            (len(self.nif_et.get()) != 9)
        ):
            self.produzir_msg_erro('Registo','Falha no registo',0)
        else:
            self.clientes.insert_last(
                Cliente(self.un_et.get(), self.pw_et.get(), self.nif_et.get())
            )
            self.user_atual = self.nif_et.get()
            self.preencher_despesas()
            self.guardar()
            #self.gestor_despesas()

    def produzir_msg_erro(self, titulo, texto, valor):
        if (valor == 0):
            return messagebox.showerror(titulo, texto)
        if (valor == 1):
            return messagebox.showinfo(titulo, texto)
            
    def login_packs(self):
        self.frame.pack()
        self.lb_login.pack(pady=40)
        self.un_lb.pack()
        self.un_et.pack()
        self.pw_lb.pack()
        self.pw_et.pack()
        self.nif_lb.pack()
        self.nif_et.pack()
        self.bt_login.pack(pady=5, ipadx=80, ipady=1)
        self.bt_sign_up.pack(pady=5, ipadx=70, ipady=1)
    
    def sign_up_packs(self):
        self.frame.pack()
        self.lb_sign_up.pack(pady=40)
        self.un_lb.pack()
        self.un_et.pack()
        self.pw_lb.pack()
        self.pw_et.pack()
        self.pw_lb_2.pack()
        self.pw_et_2.pack()
        self.nif_lb.pack()
        self.nif_et.pack()
        self.bt.pack(pady=5, ipadx=80, ipady=1)
        
    def preencher_users(self):
        self.controller.data = self.controller.ler_ficheiro_json('data.json')
        self.controller.users = self.controller.data['Clientes']
        for elemento in self.controller.users:
            self.clientes.insert_last(
                Cliente(elemento['Username'], elemento['Password'], elemento['Nif'])
            )
        self.controller.users.clear()
        
    def preencher_despesas(self):
        if not(self.despesas.is_empty()):
            for i in range(len(self.controller.users)):
                if self.controller.users[i]['Nif'] == self.user_atual:
                    for elemento in self.controller.users[i]['Userdata']:
                        self.despesas.insert_last(
                            Despesas(
                            elemento['Categoria'], 
                            elemento['Descricao'], 
                            elemento['Valor'], 
                            elemento['Data']
                            )
                        )
                self.controller.users[i]['Userdata'].clear()
    
    def guardar(self):
        if not(self.clientes.is_empty()):
            for elemento in self.clientes.dar_lista(): 
                self.controller.users.append(
                    {
                        'Username': elemento.get_username(),
                        'Password': elemento.get_password(),
                        'Nif': elemento.get_nif(),
                        'Userdata': []
                    }
                )
        if  not(self.despesas.is_empty()):
            for elemento in self.despesas.dar_lista():
                self.controller.user_data.append(
                    {
                        'Categoria':  elemento.get_categoria(),
                        'Descricao': elemento.get_descricao(),
                        'Valor':  elemento.get_valor(),
                        'Data':  elemento.get_data()
                    }
                )
            for elemento in self.controller.users:
                if elemento['Nif'] == self.user_atual: 
                    elemento['Userdata'] = self.controller.user_data
            self.controller.data['Clientes'] = self.controller.users
        self.controller.escrever_ficheiro_json('data.json',self.controller.data)
