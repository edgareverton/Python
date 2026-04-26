letras = set()
while True:
    letra = input('Digite algo:')
    letras.add(letra.lower())
    print(letras)

    if 'l' in letras:
        print('Parabêns')
        break



# # s1 = set('Edgar')
# # s1 = {'Edgar'}
# s1 = {1,2,4,5,6,7,6,6,6,66,7,7,7,7,7,7,7}
# print(s1, type(s1))

# s1 = set()
# # s2 = set()
# s1.add('Edgar')
# s1.update(('Edgar Everton', 1,2,2,3,5,4))
# print(s1)
# # print(s2)

# s1= {1,2,3}
# s2= {3,2,4}
# s3 = s1 | s2
# s4 = s1 & s2
# s5 = s2 - s1
# s6 = s1 ^ s2
# print(s6)