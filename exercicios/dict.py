import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'li': [10, 20, 30,40]
}
d2 = copy.deepcopy(d1)

print(d2,d1)
d2['li'][1] = 2000
print(d2['c1'])
print('copia\n')
print(f'este é o d1:{d1}\n\ne eate é o d2:{d2}')



# pessoa = {}

# pessoa['nome'] = 'Edgar Everton'

# print(pessoa)
# print(pessoa['nome'])

# pessoas = {
#     'nome': 'Edgar',
#     'sombrenome': 'Everton',
#     # 'idade': '100'
# }
# pessoas.setdefault('idade', 'Idade Não Exixte')

# print(pessoas['idade'])

# # print(list(pessoas.keys()))
# for chave in pessoas:
#   print(chave)

# print(list(pessoas.values()))

# for valor in pessoas:
#     # print(list(pessoas.values()))
#     print(valor)
    
# print(list(pessoas.items()))

# for chave, valor in pessoas.items():
#     print(chave, valor)