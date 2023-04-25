import tkinter as tk
from Controller import *
from model import* 


class View:
    def __init__(self):
        self.root = tk.Tk()
        self.controller = Controller()
        self.data = self.controller.ler_ficheiro_json('data.json')
        self.login_window()
        self.root.mainloop()

    def login_window(self):
        self.controller.window_geometry(self.root)
        self.main_label = tk.Label(self.root, text='Login', font='bold', pady=20)
        # username frame
        self.un_fr = tk.Frame(self.root)
        self.un_lb = tk.Label(self.un_fr, text='Username') 
        self.un_et_str = tk.StringVar()
        self.un_et = tk.Entry(self.un_fr, width=30, textvariable=self.un_et_str, bg='#c4c2bc') # hex color picker
        # password frame
        self.pw_fr = tk.Frame(self.root, pady=10)
        self.pw_lb = tk.Label(self.pw_fr, text='Password') 
        self.pw_et_str = tk.StringVar()
        self.pw_et = tk.Entry(self.pw_fr, width=30,textvariable=self.pw_et_str, show='*', bg='#c4c2bc')
        # Entry frame
        self.et_frame = tk.Frame(self.root)
        self.et_bt_in = tk.Button(self.et_frame, text="Enter", width=25)
        self.et_bt_in.config(command= lambda: self.controller.login_enter_click(self.data,self.un_et_str, self.pw_et))
        self.et_lb = tk.Label(self.et_frame)
        self.et_bt_sp = tk.Button(self.et_frame, text="Don´t have an acount yet? Sign up here", font=('','7'))
        self.et_bt_sp.config(command= lambda: self.sign_up_window(self.root))
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


    def sign_up_window(self, root):
        self.root = root
        self.root.destroy()
        self.master = tk.Tk()
        self.controller.window_geometry(self.master)

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
        self.et_bt_in.config(command=lambda:self.controller.sign_up_click(self.data,self.un_et_str,self.pw_et_str, self.pw_et_str_2))
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
        # end-loop
        self.master.mainloop()
