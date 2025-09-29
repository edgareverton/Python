condicao = True

while condicao:
    nome = input('Qual é o seu nome:')
    nome = nome.title()
    print(f'Seu nome é:{nome}')
        
    if nome == 'Sair':
            break

print('Seção terminada!')