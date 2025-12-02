
palavra_secreta = 'perfume'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra:')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra:')
        continue

    if letra_digitada in letras_acertadas:
        letras_acertadas += letra_digitada

    print(letras_acertadas)