numero_str = input('Vou dobrar o valor que vc Digitar!')

  
numero_float = numero_str = float(numero_str)
if numero_str.isdigit():
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
else:
    print('Vc não digitou um numero:')