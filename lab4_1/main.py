# Lab_4_1 main.py
# Aluno: 30011447
from functions import *
if __name__ == '__main__':
    # Exercicio 1)

    # Algumas listas
    lista_heterogenea = [1, 'Olá', 2, 'maltinha', 3]
    lista_de_numeros_reais = [2.424, 5.546, 9.12]
    lista_de_valores_duplicados = [1, 2, 9, 3, 4, 9, 1]
    lista_de_valores_int_1 = [0, 1, 2, 3, 4, 5]
    lista_de_valores_int_2 = [5, 4, 3, 2, 1, 0]

    # Exercicio 2)
    cv = input('Digite "CV" no terminal para começar: ').upper()

    if cv == 'CV':
        idade = input('Tem idade entre 25 e 45 anos?[S/N]: ').upper()
        ingles = input('Tem conhecimento de inglês?[S/N]: ').upper()
        python = input('Tem conhecimento de Python?[S/N]: ').upper()
        if (idade and ingles and python) == 'S':
            print('Pode candidatar-se à vaga.')
        else:
            print('Não possui os requisitos necessários para se candidatar a esta vagas.')

    else:
        print('Resposta inválida')
