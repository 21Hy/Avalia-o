import json
from tkinter import messagebox
import tkinter as tk

class Controller:

    def window_geometry(self, master):
        self.master = master
        # geometria centrada da janela
        self.w=300; self.h=300
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.x=(self.screen_width/2)-(self.w/2)
        self.y=(self.screen_height/2)-(self.h/2)
        self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

    def menssagem_de_erro(self, titulo, texto):
        return messagebox.showerror(titulo, texto)
    
    def sign_up_click(self,data,username,pw_1,pw_2):
        if (
            (pw_1.get() == pw_2.get()) and 
            (self.procurar_username(data, username.get())) and
            (self.verificar_inputs_sign_up(username.get(),pw_1.get()))
            ):
            self.adicionar_cliente(data,username.get(),pw_1.get())
            print('Deu certo o sign up')
        else:
            self.menssagem_de_erro('Erro', 'Username existente ou passord incorreta.')

    def login_enter_click(self,data,username,password):
        if self.login_validacao(data,username.get(),password.get()): # alterar
            print('Deu certo o login')
        else:
            self.menssagem_de_erro('Erro','Username ou password incorretos')

    def escrever_ficheiro_json(self,nome_ficheiro, data):
        self.json_string = json.dumps(data, indent = 2)
        self.json_file = open(nome_ficheiro, 'w')
        self.json_file.write(self.json_string)
        self.json_file.close()

    def ler_ficheiro_json(self,nome_ficheiro):
        with open(nome_ficheiro, 'r') as f:
            self.data = json.load(f)
        return self.data
    
    def adicionar_cliente(self, data, username, password):
        data['Clientes'].append({'Username':username, 'Password':password, 'Userdata': {}})
        self.escrever_ficheiro_json('data.json',data)
        self.login_validacao(data,username,password)
    # para o sign-up
    def procurar_username(self, data, username):
        for elemento in data['Clientes']:
            if elemento['Username'] == username:
                return False
        return True
    # para o login enter
    def login_validacao(self, data, username, password):
        for i in range(len(data['Clientes'])):
            if (
                (data['Clientes'][i]['Username'] == username) and 
                (data['Clientes'][i]['Password'] == password)
                ):
                self.user_data = data['Clientes'][i]['Userdata']
                self.data_indice = i
                return True
        return False
    
    def guardar_alteracoes(self):
        self.data['Cientes'][self.data_indice]['Userdata'] = self.user_data

    def verificar_inputs_sign_up(self,username,password):
        if (
            (len(username) >= 4) and
            (len(password) >= 4)
            ):
            return True
        else:
            return False
