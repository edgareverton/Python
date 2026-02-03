# pessoa = {}

# pessoa['nome'] = 'Edgar Everton'

# print(pessoa)
# print(pessoa['nome'])

pessoas = {
    'nome': 'Edgar',
    'sombrenome': 'Everton',
    # 'idade': '100'
}
pessoas.setdefault('idade', 'Idade Não Exixte')

print(pessoas['idade'])

# print(list(pessoas.keys()))
# for chave in pessoas:
#   print(chave)

# print(list(pessoas.values()))

# for valor in pessoas:
#     # print(list(pessoas.values()))
#     print(valor)
    
# print(list(pessoas.items()))

# for chave, valor in pessoas.items():
#     print(chave, valor)