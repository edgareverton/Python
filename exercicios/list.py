#exercicio 1
# lista = [123, True, 'Edgar Everton', [], 1.5] 

# lista[2] = 'Olá Mundo'
# print(lista)

# #exercicio 2
# lista = [120, 30, 45, 50, 100]
# #del lista[2]
# #lista[3] = 500
# # lista.append(600)
# # lista.insert(1, 24)

# # print(lista)

#exercicio 3
# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_r = 'jfgh'
# #lista_c = lista_a + lista_b
# #lista_p = lista_a.extend(lista_r)
# lista_a.extend(lista_r)
# print(lista_a)

#exercicio 4
#exiba os índices da lista
# 0 Maria
# 1 Helena
# 2 Luiz

lista = ['Maria', 'Helena', 'Luíz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])