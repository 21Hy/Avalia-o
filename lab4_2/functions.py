# função de confirmar o input do jogador
def confirmar_input(input):
    if ((input == ('pedra') ) or (input == ('papel')) or (input == ('tesoura'))):
        return True
    else:
        return False

# função de decidir a pontuação
def decidir(lista):
    # vairiáveis de pontuação
    x = 0
    y = 0
    # condições vituriosas para primeiro jogador
    if ((lista == ['tesoura', 'papel']) or (lista == ['pedra', 'tesoura']) or (lista == ['papel', 'pedra'])):
        x += 5
    # condições vituriosas para segundo jogador
    if ((lista == ['papel', 'tesoura']) or (lista == ['tesoura', 'pedra']) or (lista == ['pedra', 'papel'])):
        y += 5
    # condições de empate
    if ((lista == ['tesoura', 'tesoura']) or (lista == ['pedra', 'pedra']) or (lista == ['papel', 'papel'])):
        x += 1
        y += 1
    return x, y
