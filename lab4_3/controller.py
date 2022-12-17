from model import*

def adicionar_presentes(lista):
    lista_geral.clear()
    lista_geral.extend(lista)
    return lista_geral

def verificar_input_valor(valor):
    lista_de_valores_possiveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for elemento in str(valor).split():
        if elemento in lista_de_valores_possiveis:
            return True

def verificar_correspondecia(valor, lista):
    for elemento in lista:
        if len(lista) == int(valor):
            return True
        else:
            return False

def retirar_presentes(lista):
    for elemento in lista:
        if elemento in lista_geral:
            lista_geral.remove(elemento)
        else:
            break
    return lista_geral



 