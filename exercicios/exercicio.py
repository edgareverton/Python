import os

# Função completa do desafio
def stemmer(text):
    # Separa a string em uma lista de palavras baseada nos espaços
    words = text.split(' ')
    processed_words = []

    for word in words:
        # REGRA 1: Remover sufixos ('ed', 'ly', 'ing')
        # Utilizamos if/elif para garantir que apenas um sufixo seja removido por vez
        if word.endswith('ed'):
            word = word[:-2]  # Remove os 2 últimos caracteres
        elif word.endswith('ly'):
            word = word[:-2]  # Remove os 2 últimos caracteres
        elif word.endswith('ing'):
            word = word[:-3]  # Remove os 3 últimos caracteres
        
        # REGRA 2: Truncar se for maior que 8 caracteres
        if len(word) > 8:
            word = word[:8]  # Mantém apenas do índice 0 até o 7
            
        processed_words.append(word)

    # Junta a lista de volta em uma única string separada por espaços
    return " ".join(processed_words)

# Bloco de execução principal
if __name__ == '__main__':
    # Verifica se a variável de ambiente existe (comum em plataformas como HackerRank)
    # Se estiver rodando localmente, você pode comentar as linhas de arquivo e usar print()
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        
        # Lê a entrada
        text_input = input()
        
        # Chama a função
        result = stemmer(text_input)
        
        # Escreve o resultado
        fptr.write(result + '\n')
        fptr.close()
    else:
        # Modo de teste local (caso não esteja na plataforma de desafio)
        text_input = input("Digite o texto para teste: ")
        print(stemmer(text_input))