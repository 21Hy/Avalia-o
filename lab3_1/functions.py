import random
#import emoji

def gerar():
    num = random.randint (1,100)
    if num > 10:
        return True
    else:
        return False

def substituir(palavra):
    substituicao = palavra.replace('a', 'x')
    return substituicao

def verificar_numero(number):
    if type(number) == float:
        return round(number)
    else:
        return False

def retornar_emoji(palavra):
    if palavra == 'feliz':
        return '\U0001F600'
    
    else: 
        return '\U0001F610'





