# exercicio 1, a)
def mesmo_tamanho(lista1, lista2):
    if len(lista1) == len(lista2):
        return True

# exercicio 1, b)
def valores_repetidos(lista1): ###
    pass

# exercicio 1, c)
def soma_do_primeiro_e_ultimo(lista):
    # dúvida, receber em números inteiros ou float em functions???
    return lista[0] + lista[len(lista) - 1]

# exercicio 1, d)
def soma_de_duas_listas_com_o_mesmo_indice(lista1, lista2): ###
    # dúvida, receber em números inteiros ou float em functions???
    if len(lista1) > len(lista2):
        for i in range(len(lista1)):
            return lista1[i] + lista2[i]
    else: 
        for i in range(len(lista2)):
            return lista1[i] + lista2[i]

# exercicio 1, e)

# exercicio 1, f)
def media_dos_valores_da_lista(lista):
    for i in range(len(lista)):
        lista[i]
