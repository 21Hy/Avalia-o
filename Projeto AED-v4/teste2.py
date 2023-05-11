class Cliente:
    def __init__(self, nome, password):
        self.__nome = nome
        self.__password = password

    def get_nome(self):
        return self.__nome
        
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        
    def get_password(self):
        return self.__password
        
    def set_password(self, nova_password):
        self.__password = nova_password



cliente_02 = Cliente('Jorge','34')
cliente_03 = Cliente('Zé', '53')

cliente_01 = Cliente('Luis','21')


def ar(nome_variavel, objeto):
    nome_variavel = objeto
    return nome_variavel

print(ar(cliente_01.get_nome(), cliente_01))



