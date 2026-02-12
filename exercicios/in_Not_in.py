nome = input('Digite seu nome:')
encontrar = input('Digite o que vc quer encontrar:')

if encontrar in nome:
    print(f'"{encontrar}"estar entre "{nome}"')
else:
    print(f"Não estar entre {nome}")