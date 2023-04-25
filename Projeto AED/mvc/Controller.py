import json
from tkinter import messagebox
import tkinter as tk

class Controller:
    def __init__(self, master):
        self.master = master
        self.login_window(self.master)

    def login_window(self, master):
        self.window_geometry()
        self.main_label = tk.Label(master, text='Login', font='bold', pady=20)
        # username frame
        self.un_fr = tk.Frame(master)
        self.un_lb = tk.Label(self.un_fr, text='Username') 
        self.un_et_str = tk.StringVar()
        self.un_et = tk.Entry(self.un_fr, width=30, textvariable=self.un_et_str, bg='#c4c2bc') # hex color picker
        # password frame
        self.pw_fr = tk.Frame(master, pady=10)
        self.pw_lb = tk.Label(self.pw_fr, text='Password') 
        self.pw_et_str = tk.StringVar()
        self.pw_et = tk.Entry(self.pw_fr, width=30,textvariable=self.pw_et_str, show='*', bg='#c4c2bc')
        # Entry frame
        self.et_frame = tk.Frame(master)
        self.et_bt_in = tk.Button(self.et_frame, text="Enter", width=25)
        self.et_bt_in.config(command= lambda: self.login_click(self.un_et_str, self.pw_et))
        self.et_lb = tk.Label(self.et_frame)
        self.et_bt_sp = tk.Button(self.et_frame, text="Don´t have an acount yet? Sign up here", font=('','7'))
        self.et_bt_sp.config(command= self.sign_up_window)
        # packs
        self.main_label.pack()
        self.un_fr.pack()
        self.un_lb.pack()
        self.un_et.pack()
        self.pw_fr.pack()
        self.pw_lb.pack()
        self.pw_et.pack()
        self.et_frame.pack()
        self.et_bt_in.pack()
        self.et_lb.pack()
        self.et_bt_sp.pack()

    def sign_up_window(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.window_geometry()

        self.main_label = tk.Label(self.master, text='Sign-up', font='bold', pady=20)
        # username frame
        self.un_fr = tk.Frame(self.master)
        self.un_lb = tk.Label(self.un_fr, text='Username') # hex color picker
        self.un_et_str = tk.StringVar()
        self.un_et = tk.Entry(self.un_fr, width=30, textvariable=self.un_et_str, bg='#c4c2bc')
        # password frame
        self.pw_fr = tk.Frame(self.master, pady=10)
        self.pw_lb = tk.Label(self.pw_fr, text='Password') # hex color picker
        self.pw_et_str = tk.StringVar()
        self.pw_et = tk.Entry(self.pw_fr, width=30,textvariable=self.pw_et_str, show='*', bg='#c4c2bc')
        # password frame
        self.pw_lb_2 = tk.Label(self.pw_fr, text='Confirm assword') # hex color picker
        self.pw_et_str_2 = tk.StringVar()
        self.pw_et_2 = tk.Entry(self.pw_fr, width=30,textvariable=self.pw_et_str_2, show='*', bg='#c4c2bc')
        # Entry frame
        self.et_fr = tk.Frame(self.master)
        self.et_bt_in = tk.Button(self.et_fr, text="Enter", width=25)
        self.et_bt_in.config(command=lambda:self.sign_up_click(self.pw_et_str, self.pw_et_str_2))
        # packs
        self.main_label.pack()
        self.un_fr.pack()
        self.un_lb.pack()
        self.un_et.pack()
        self.pw_fr.pack()
        self.pw_lb.pack()
        self.pw_et.pack()
        self.pw_lb_2.pack()
        self.pw_et_2.pack()
        self.et_fr.pack()
        self.et_bt_in.pack()
        # end loop 
        self.master.mainloop()

    def main_window(self):
        self.master.destroy()
        self.master = tk.Tk()

        self.master.mainloop()

    def login_click(self, string_1, string_2):
        if string_1.get() == string_2.get(): # alterar
            self.main_window()
        else:
            messagebox.showerror('Erro', 'Falha no login')

    def sign_up_click(self, string_1, string_2):
        if string_1.get() == string_2.get():
            pass
        else:
            messagebox.showerror('Erro', 'Username existente ou passowrd incorreta')


    def escrever_ficheiro_json(self,nome_ficheiro, data):
        self.json_string = json.dumps(data, indent = 2)
        self.json_file = open(nome_ficheiro, 'w')
        self.json_file.write(self.json_string)
        self.json_file.close()

    def ler_ficheiro_json(self,nome_ficheiro):
        with open(nome_ficheiro, 'r') as ficheiro:
            self.data = json.load(ficheiro)
        return self.data
    
    def ligar(self, root):
        self.new_root = tk.Toplevel(root)

    def window_geometry(self):
        self.w=400; self.h=300
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.x=(self.screen_width/2)-(self.w/2)
        self.y=(self.screen_height/2)-(self.h/2)
        self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

