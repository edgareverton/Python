frase = ' Esta é uma frase somente para ' \
'contagem de palavras no python' \
' nada de mais né kkkkk'

i = 0 
qtd_apareceu_mais_vezes = 0
letra_q_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_q_apareceu_mais_vezes = letra_atual
   
    i += 1

print   (
          'A letra que apareeu mais vezes foi '
          f'"{letra_q_apareceu_mais_vezes }" que apareceu '
          f'{qtd_apareceu_mais_vezes} x'
         )