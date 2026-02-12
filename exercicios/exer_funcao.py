def multiplicar_tudo(*args):
   
    total = 1
    for numero in args:
        total *= numero
    return total
resultado = multiplicar_tudo(1,2,3,4,5)

print(f'O resultado final é: {resultado}')


def impar_par(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'
print(impar_par(5))
print(impar_par(6))
print(impar_par(3))
print(impar_par(10))