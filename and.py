entrar = input('Digite [E] para ENTRAR e [S] para SAIR ')

senha_digitada = input('Digite sua senha: ')
senha_permitida = '123'

if entrar == 'E' and senha_digitada == senha_permitida:
    print('Você entrou:')

else:
    print('Você saiu!')
