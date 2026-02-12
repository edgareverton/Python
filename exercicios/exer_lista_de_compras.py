import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]inserir [a]apagar [l]listar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por Favor digite número inteiro')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para Listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor digite "i", "a" ou "l" ')