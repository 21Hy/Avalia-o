from functions import *
if __name__ == '__main__':

    print('''
        ------Bem vindo ao meu jogo------''')
    
    biblioteca_de_informação = [{'Nome': 'jogador1', 'Pontuação': 0}, {'Nome': 'jogador2', 'Pontuação': 0 }]

    while True:
        instrucao_principal = input('''
        -----Menu Principal-----
        [RJ] para Registar jogadores
        [IJ] para Inciar Jogo 
        [VP] para Visualizar Pontuação
        [S] para Sair
        :  ''').upper()

        if instrucao_principal == 'RJ':
            print('''
        -Menu de Registo-''')
            biblioteca_de_informação[0]['Nome'] = input('''
        Registar como jogador 1: ''')
            biblioteca_de_informação[1]['Nome'] = input('''
        Registar como jogador 2: ''')

        elif instrucao_principal == 'IJ':
            print(f'''
        -Menu de Jogo-
        Jogador 1: {biblioteca_de_informação[0]['Nome']}
        Jogador 2: {biblioteca_de_informação[1]['Nome']} ''')
            while True:
                escolha1 = input(f'''
        Digita a sua jogada {biblioteca_de_informação[0]['Nome']} 
        [pedra/papel/tesoura]: ''').lower()

                escolha2 = input(f'''
        Digita a sua jogada {biblioteca_de_informação[1]['Nome']} 
        [pedra/papel/tesoura]: ''').lower()

                if (confirmar_input(escolha1) and confirmar_input(escolha2)):
                    resultado_da_escolha1, resultado_da_escolha2 = decidir([escolha1, escolha2])
                    biblioteca_de_informação[0]['Pontuação'] += resultado_da_escolha1
                    biblioteca_de_informação[1]['Pontuação'] += resultado_da_escolha2
                    break
                else:
                    print('''
            ...Instrução Inválida...
            ''')

        elif instrucao_principal == 'VP': 
            print(f'''
        -Menu de Pontuação-
        {biblioteca_de_informação}
        ...
        Jogador 1: {biblioteca_de_informação[0]['Nome']}, Pontuação: {biblioteca_de_informação[0]['Pontuação']}
        Jogador 2: {biblioteca_de_informação[1]['Nome']}, Pontuação: {biblioteca_de_informação[1]['Pontuação']}''')

        elif instrucao_principal == 'S':
            print('''
        ------Adeus------''')
            break

        else:
            print('''
            ...Instrução Inválida...
            ''')
