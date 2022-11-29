from functions import *

if __name__ == '__main__':
    ################Exercicio 1#####################
    resultado = gerar()

    if resultado == True:
        print ('O número é maior do que 10')
    else:
        print ('O número é igual ou menor do que 10.')

    ###############################################
    ################Exercicio 2#####################

    palavra = input('Digita a tua palavra: ').lower()
    resultado_2 = substituir(palavra)
    print ('A nova palavra é: ', resultado_2 )

    ###############################################
    ################Exercicio 3#####################

    number_1 = 1 
    number_2 = 2.5
    print ('O resultado é: ', verificar_numero(number_1))
    print ('O resultado é: ', verificar_numero(number_2))

    ###############################################
    ################Exercicio 4#####################
    palavra_2 = input('Palavra: ').lower
    print(retornar_emoji(palavra_2))

    ###############################################