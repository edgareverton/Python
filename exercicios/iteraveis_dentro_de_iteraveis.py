salas = [
    ['João', 'Maria', 'Ítalo'],
    ['Eduarda'],
    ['Bosco', 'Edgar', 'Peter']
]
nada = 'ola'
# print(sala[0][1])
# print(sala[2][3][2])
for sala in salas:
    print(f'A sala é: {sala}')
    for aluno in sala:
        print(f'- {aluno} -')