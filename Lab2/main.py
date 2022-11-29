from functions import *

if __name__ == '__main__':
    #########Exercício 1##############
    cena = input('escreve aqui\n')
    print (len(cena))


    ######################################
    #########Exercício 2##################
    cena_2 = input('escreve aqui\n')
    print (cena_2.lower())


    ######################################
    #########Exercício 3##################
    cena_3 = importar('Porto','Lisboa')
    print (cena_3)


    ######################################
    #########Exercício 4##################
    cena_4 = retornar ('programar')
    print(cena_4 + str( len(cena_4)))


    ######################################
    #########Exercício 5##################
    cena_5 = int(input('Quantos imóvies vendeu este mês?\n'))
    cena_5b = calcular (cena_5)
    print ('O seu salário mensal é: salário base com acréscimo de', cena_5b)


    ######################################