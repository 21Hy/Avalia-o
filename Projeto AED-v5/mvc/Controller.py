import json

class Controller:
    def __init__(self, master):
        self.master = master
        self.data = None
        self.users = None
        self.user_data = []

    def escrever_ficheiro_json(self,nome_ficheiro, data):
        self.json_string = json.dumps(data, indent = 2)
        self.json_file = open(nome_ficheiro, 'w')
        self.json_file.write(self.json_string)
        self.json_file.close()

    def ler_ficheiro_json(self,nome_ficheiro):
        with open(nome_ficheiro, 'r') as f:
            self.data = json.load(f)
        return self.data


    

