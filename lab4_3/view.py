from controller import*

def main():

    # Inicio, pergunta ao utilizador se é noivo ou convidado
    while True:
        pergunta_incial = input('''
-----Menu Inicial-----
1. Noivo
2. Convidado
3. Sair
: ''').upper()
            
        if pergunta_incial == '1':
            while True:
                escolha_noivos = input('''
-Menu Noivos-
CLC - Criar lista de casamento
ELC - Eliminar presentes
MI - Menu Inicial
: ''') .upper()
                if escolha_noivos == 'CLC':
                    while True:

                        while True:
                            escolha_cls_1 = input('Número de presente(s): ')
                            if verificar_input_valor(escolha_cls_1):
                                break
                            else:
                                print('[Número de presente(s) não correspondido]')

                        while True:
                            escolha_cls_2 = input('Nome(s) do(s) presente(s): ').split()
                            if verificar_correspondecia(escolha_cls_1, escolha_cls_2):
                                break
                            else:
                                print('[Número de presente(s) não correspondido]')
                                break
                        if (verificar_input_valor(escolha_cls_1)) and (verificar_correspondecia(escolha_cls_1, escolha_cls_2)):
                            break

                    print(f'''
[Adicionado com Sucesso]
{adicionar_presentes(escolha_cls_2)}''')
                    
                elif escolha_noivos == 'ELC':
                    escolha_elc = input('Nome(s) do(s) presente(s): ').split()
                    retirar_presentes(escolha_elc)
                    print(lista_geral)

                elif escolha_noivos == 'MI':
                    break

                else:
                    print('...Resposta Inválida...')
        

        elif pergunta_incial == '2':
            while True:
                escolha_convidados = input('''
-Menu Convidados-
VLC - Ver lista de presentes de casamento
SP - Seleção do presente a comprar
MI - Menu Inicial
: ''').upper() 
                if escolha_convidados == 'VLC':
                    print(lista_geral)

                elif escolha_convidados == 'SP':
                    while True: 

                        while True:
                            escolha_convidados_sp_1 = input('Número de presente(s) a comprar: ')
                            if verificar_input_valor(escolha_convidados_sp_1):
                                break
                            else:
                                print('[Número de presente(s) não correspondido]')


                        while True:
                            escolha_convidados_sp_2 = input('Nome(s) do(s) presente(s) a comprar: ').split()
                            if verificar_correspondecia(escolha_convidados_sp_1, escolha_convidados_sp_2):
                                break
                            else:
                                print('[Número de presente(s) não correspondido]')
                                break

                        if (verificar_input_valor(escolha_convidados_sp_1)) and (verificar_correspondecia(escolha_convidados_sp_1, escolha_convidados_sp_2)):
                            break
                    print(retirar_presentes(escolha_convidados_sp_2))
                    
                elif escolha_convidados == 'MI':
                    break

                else:
                    print('...Resposta Inválida...')

        elif pergunta_incial == '3':
            break

        else:
            print('...Resposta Inválida...')