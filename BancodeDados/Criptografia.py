import numpy as np

#dicionario para conversao
dic_modulo29 = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
    'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26,
    ',': 27, '.': 28
}

#dicionario inverso
dic_modulo29_inverso = {v: k for k, v in dic_modulo29.items()}

def cripto(descricao):
    #matriz chave e inicia nulo
    matriz_chave = [2, 1, 1, 1]
    modulo_29 = []
    modulo_29_cripto = []
    frase_cripto = ''
    #fazer virar par
    if len(descricao) % 2 == 1:
        descricao += ' '
    #converte para numero e colocar em lista
    for l in descricao.upper():
        if l in dic_modulo29:
            modulo_29.append(dic_modulo29[l])
    #vira matriz
    matrizFrase = np.array(modulo_29).reshape(2, -1)
    matrizChave = np.array(matriz_chave).reshape(2, -1)
    #multiplicar matriz pela chave
    matriz_cripto = np.matmul(matrizChave, matrizFrase)
    #aplica modulo 29
    for j in matriz_cripto:
        for i in range(0, len(j)):
            j[i] = j[i] % 29
            modulo_29_cripto.append(j[i])
    #converte em letras novamente
    for n in modulo_29_cripto:
        if n in dic_modulo29_inverso:
            frase_cripto += dic_modulo29_inverso[n]
    #retorna a frase criptografada para ser inserida no banco
    return frase_cripto

def descripto(descricao):
    #inicia nulo
    matriz_chave = [1, -1, -1, 2]
    modulo_29 = []
    modulo_29_cripto = []
    frase_cripto = ''
    #converte em numero
    for l in descricao:
        if l in dic_modulo29:
            modulo_29.append(dic_modulo29[l])
    #faz matriz
    matrizFrase = np.array(modulo_29).reshape(2, -1)
    matrizChave = np.array(matriz_chave).reshape(2, -1)
    #multiplicar matriz pela chave
    matriz_descripto = np.matmul(matrizChave, matrizFrase)
    #aplica modulo 29
    for j in matriz_descripto:
        for i in range(0, len(j)):
            j[i] = j[i] % 29
            modulo_29_cripto.append(j[i])
    #converte em letras
    for n in modulo_29_cripto:
        if n in dic_modulo29_inverso:
            frase_cripto += dic_modulo29_inverso[n]
    #retorna frase descriptografada
    return frase_cripto

#frase = cripto("Hello?&#!")
#print(frase)
#desc = descripto(frase)
#print(desc)
#'!': 29, ':': 30, ';': 31, '?': 32, '@': 33, '#': 34, '$': 35, 'É': 36, 'Á': 37, 'À': 38, 'Ú': 39, '&': 40