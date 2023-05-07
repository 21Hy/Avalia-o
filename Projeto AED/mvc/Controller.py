import json
from tkinter import messagebox

class Controller:
    def __init__(self, master):
        self.master = master
        self.data = self.ler_ficheiro_json('data.json')
        self.user_data = None # data do user depois do login
        self.data_indice = None # irá guardar o indice em que o user se encontra dentro da lista de dicts
    
    def sign_up_click(self,username,pw_1,pw_2,nif):
        if (
            (pw_1.get() == pw_2.get()) and 
            (self.procurar_username(username.get())) and
            (self.verificar_inputs_sign_up(username.get(),pw_1.get(),nif.get()))
            ):
            self.adicionar_cliente(username.get(),pw_1.get(),nif.get())
            print('Deu certo o sign up')
        else:
            self.produzir_msg_erro('Erro', 'Username existente ou passord incorreta.')

    def login_enter_click(self, username, password, nif):
        if self.login_validacao(username.get(), password.get(), nif.get()):
            print('Deu certo o login')
        else:
            self.produzir_msg_erro('Erro','Username ou password incorretos')

    def escrever_ficheiro_json(self,nome_ficheiro, data):
        self.json_string = json.dumps(data, indent = 2)
        self.json_file = open(nome_ficheiro, 'w')
        self.json_file.write(self.json_string)
        self.json_file.close()

    def ler_ficheiro_json(self,nome_ficheiro):
        with open(nome_ficheiro, 'r') as f:
            self.data = json.load(f)
        return self.data
    
    def adicionar_cliente(self, username, password, nif):
        self.data['Clientes'].append({'Username':username, 'Password':password,'Nif':nif,'Userdata': {}})
        self.escrever_ficheiro_json('data.json',self.data)
        self.login_validacao(username,password,nif)
    # para o sign-up
    def procurar_username(self, username):
        for elemento in self.data['Clientes']:
            if elemento['Username'] == username:
                return False
        return True
    # para o login enter
    def login_validacao(self,username, password, nif):
        for i in range(len(self.data['Clientes'])):
            if (
                (self.data['Clientes'][i]['Username'] == username) and 
                (self.data['Clientes'][i]['Password'] == password) and
                (self.data['Clientes'][i]['Nif'] == nif)
                ):
                self.user_data = self.data['Clientes'][i]['Userdata']
                self.data_indice = i
                return True
        return False
    
    def guardar_alteracoes(self):
        self.data['Cientes'][self.data_indice]['Userdata'] = self.user_data

    def verificar_inputs_sign_up(self,username,password,nif):
        if (
            (len(username) >= 4) and
            (len(password) >= 4) and
            (len(nif) == 9)
            ):
            return True
        else:
            return False
        
    def produzir_msg_erro(self, titulo, texto):
        # produz uma mensagem de erro numa janela oferecida pelo módulo tkinter
        return messagebox.showerror(titulo, texto)
    
