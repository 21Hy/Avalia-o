#       Exercicio 2 projeto 'super calculadora'
#       Aluno: 30011447

from functions import*

if __name__ == '__main__':

    while True:
        print('''
                Olá seja bem vindo(a) à SUPER CALCULADORA,
                por favor escolha uma das seguintes opções abaixo
                
                1. Somar dois números;
                2. Multiplicar dois números;
                3. Comparar números;
                4. Verificar igualdade;
                5. Retornar o maior de dois números;
                6. Retornar o menor de dois números. ''')
        
        opcao_escolhida = input('Digita aqui a sua opção: ')
        
        if opcao_escolhida == '1':
            num1 = float(input('Primeiro número: '))
            num2 = float(input('Segundo número: '))
            print(somar_numeros(num1, num2))
        
        elif opcao_escolhida == '2':
            num1 = float(input('Primeiro número: '))
            num2 = float(input('Segundo número: '))
            print(multiplicar_numeros(num1, num2))

        elif opcao_escolhida == '3':
            num1 = float(input('Primeiro número: '))
            num2 = float(input('Segundo número: '))
            valor_retornado = comparar_numeros(num1, num2)
            if valor_retornado == True:
                print('O primeiro número indicado é maior do que o segundo')
            elif valor_retornado == False:
                print('O primeiro número indicado é menor do que o segundo')
            else:
                print('Os números são iguais')

        elif opcao_escolhida == '4':
            num1 = float(input('Primeiro número: '))
            num2 = float(input('Segundo número: '))
            valor_retornado_2 = verificar_igualdade(num1, num2)
            if valor_retornado_2 == True:
                print('Os dois números são iguais')
            else:
                print('Os números são diferentes')

        elif opcao_escolhida == '5':
            num1 = float(input('Primeiro número: '))
            num2 = float(input('Segundo número: '))
            print(retornar_maior_de_dois(num1, num2))

        elif opcao_escolhida == '6':
            num1 = float(input('Primeiro número: '))
            num2 = float(input('Segundo número: '))
            print(retornar_menor_de_dois(num1, num2))
        
        elif opcao_escolhida == '7':
            break

        else:
            print('Instrução inválida')
        
        print('''
                7. Sair ''')
