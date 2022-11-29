############# Funções Exercício 1 #############
def funcao_1():
    for i in range(-10, 10, 2):
        if (i%2 == 0):
            return i
## Indique o quais as operações realizadas pela função e o respetivo é o resultado.
#Resposta:
#       A função tem consigo um ciclo reptetitivo com um contador automático com um alcance 
#       de -10 a 10, utilizando a função range, incrementando 2 a 2 (não contando o 10). Este ciclo 
#       está associado à variável 'i' que é retornada se o resto da mesma ,a dividir por 2, for 0. A
#       função deverá apresentar esta resposta:
#       -10
#       -8
#       -6
#       -4
#       -2
#       0
#       2
#       4
#       6
#       8

#################################################
def funcao_2(numero):
    n = 0
    while n < numero:
        numero *= 2
    return numero
## Indique o quais as operações realizadas pela função e o respetivo é o resultado.
#Resposta:
#       A função tem como parametro de entrada a variável numero, esta que passa por um ciclo while 
#       que vai erificar se esse número é menor que 0. Caso seja, esse número será multiplciso por 2
#       infinitivamente e retornado, caso não seja a função vai limitar-se a retornar esse mesmo número.

#################################################
def funcao_3(palavra):
    for i in range(len(palavra)):
        if palavra[0] == 'a':
            palavra.replace('a', 'c')
        else:
            palavra.replace(palavra[0], 'x')
        
        return palavra
## Indique o quais as operações realizadas pela função e o respetivo é o resultado.
#Resposta:
#       A função tem como paramtro a entrada a palavra 'palavra' esta que o seu comprimento
#       (um número inteiro) terá uso no alcance do ciclo 'for' (como terá só um argummento irá 
#       assumir o alcance de 0 a comprimento da 'palavra' com incrementação feita de 1 em 1).
#       Já dentro do ciclo a palavra passa por diversas verificações. Se o primeiro caracter da
#       palavra for 'a' então essa mesma letra é trocada por um 'c'. Caso não ser um 'a' então o 
#       primeiro caracter será substituido por 'x'. No entanto todas estas condições parecem inúteis 
#       dado que o valor retornado será só o parametro inical, não surtindo efeito qualquer condição 
#       imposta.
#       

#################################################
def funcao_4():
    for i in range(10, 20, -1):
        return i
## Indique o quais as operações realizadas pela função e o respetivo é o resultado.
#Resposta:
#       A função contem um ciclo 'for' com a função range associada. Esta função tem como argumentos:
#       parametro inicial 10 e final 20 incrementando de -1 a -1, no entanto como o parametro final é
#       menor que o parametro final e dada a variável de incrementação (-1) a função irá tender para
#       menos infinito.

#################################################

############# Funções Exercício 2 #############

def somar_numeros(numero_1, numero_2):
    return numero_1 + numero_2

def multiplicar_numeros(numero_1, numero_2):
    return numero_1 * numero_2

def comparar_numeros(numero_1, numero_2):
    #Tarefa: Completar a função
    #Objetivo da função: comparar dois números entre si 
    if numero_1 > numero_2:
        return True
    elif numero_1 < numero_2:
        return False

def verificar_igualdade(numero_1, numero_2):
    if numero_1 == numero_2:
        return numero_1

def retornar_maior_de_dois(numero_1, numero_2):
    #Tarefa: Completar a função
    #Objetivo da função: comparar dois números e retornar o número maior
    if numero_1 > numero_2:
        return numero_1
    else:
        return numero_2

def retornar_menor_de_dois(numero_1, numero_2):
    if numero_1 < numero_2:
        return numero_1
    else:
        return numero_2
