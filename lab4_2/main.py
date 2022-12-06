# lab4_2 Jogo Pedra, Papel ou Tesoura.
# Aluno: 30011447

from functions import *
if __name__ == '__main__':

 

    # Parte 1 - Registar jogador - 
    print('''
            --------Bem vindo ao jogo--------
            Este é uma versão do jogo de pedra papel ou tesoura, 
            terá um total de 10 rondas, por ronda uma vitória corres-
            ponde a 5 pontos, uma derrota a 0 pontos e empate 1 ponto. 
             ''')
    jogador1 = input('Nome do primeiro jogador: ')
    jogador2 = input('Nome do segundo jogador: ')

    for i in range(1, 10):
        # Parte 2 - Inciar o jogo -
        print(f'''
        Ronda número {i}
        Jogador 1: "{jogador1}" 
        jogador 2: "{jogador2}
        Para sair: "sair"
        Visualizar a pontuação: VP''')
        
        primeira_jogada = input(f'Faz a tua jogada {jogador1} [Pedra/Papel/Tesoura]: ').lower()
        segunda_jogada = input(f'Faz a tua jogada {jogador2} [Pedra/Papel/Tesoura]: ').lower()

        jogada(primeira_jogada, segunda_jogada)

