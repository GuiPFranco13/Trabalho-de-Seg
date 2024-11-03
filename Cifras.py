#Cifra de Deslocamento (Cifra de César)

def cifra_deslocamento(txt, desloca): #Para funcionar, deve se ceder também qual o deslocamento que será utilizado
    resultado = ""

    for char in txt:
        if char.isalpha(): #Verifica se o caractere é uma letra
            deslocamento_base = 65 if char.isupper() else 97 #Define a base de deslocamento para maiusculas e minusculas
            resultado += chr((ord(char) - deslocamento_base + desloca) % 26 + deslocamento_base)
        else:
            resultado += char #Mantem caracteres não alfabeticos inalterados

    return resultado

#Quebra da Cifra por Força Bruta

def forca_bruta(cifra):

    for deslocamento in range(1, 26): #Testa todos os possíveis deslocamentos de 1 a 25

        resultado = ""
        for char in cifra:
            if char.isalpha():
                deslocamento_base = 65 if char.isupper() else 97

                resultado += chr((ord(char) - deslocamento_base - deslocamento) % 26 + deslocamento_base)
            
            else:
                resultado+= char
        print(f"Deslocamento {deslocamento}: {resultado}") #Retorna o resultado junto do deslocamento

#Quebra de Cifra por Distribuição de Frequência

from collections import Counter #Para facilitar o desenvolvimento do código, utilizei o Counter para contar a frequência

def decifrador(cifra, deslocamento):#Foi criado um decifrador básico para utilizar pós analise de freqência

    resultado = ""
    for char in cifra:
        if char.isalpha():
            deslocamento_base = 65 if char.isupper() else 97
            resultado += chr((ord(char) - deslocamento_base - deslocamento) % 26 + deslocamento_base)
        else:
            resultado+=char
    return resultado

def frequencia(cifra):
    
    frequencias = Counter(cifra) #Conta a frequencia de cada caractere presnete na cifra
    mais_comum = frequencias.most_common(1)[0][0] #Encontra qual o caractere mais comum
    deslocamento = (ord(mais_comum) - ord('a')) % 26 #Supondo que a letra A é a mais comum do português
    return decifrador(cifra, deslocamento)


#Cifra de Transposição

def cifra_transposicao(txt, chave): #A chave é definida por que for utilizar o código
    colunas = [''] * chave #Cria uma lista de strings vazias, uma para cada coluna

    for coluna in range(chave):
        indice = coluna
        while indice < len(txt):
            colunas[coluna] += txt[indice] #Adiciona um caractere a coluna correspondente

            indice+=chave #Move o indice pra próxima coluna

    return ''.join(colunas) #Junta todas as colunas e forma o texto cifrado

#Quebra da Cifra por Analise de Texto Cifrado

def transposicao(txt, chave):
    num_linhas = len(txt) // chave  # Calcula o número de linhas completas
    num_colunas = chave  # O número de colunas é a chave
    num_vazios = len(txt) % chave  # Calcula o número de colunas que têm um caractere a menos

    colunas = [''] * num_colunas
    indice = 0

    for coluna in range(num_colunas):
        num_caracteres = num_linhas + (1 if coluna < num_vazios else 0)  #Calcula o número de caracteres em cada coluna
        colunas[coluna] = txt[indice:indice + num_caracteres]  #Preenche a coluna com os caracteres correspondentes
        indice += num_caracteres

    resultado = ''
    for linha in range(num_linhas + 1):
        for coluna in range(num_colunas):
            if linha < len(colunas[coluna]):
                resultado += colunas[coluna][linha]  #Reconstroi o texto original linha por linha

    return resultado

def forca_bruta_transposicao(txt_cifrado, max_chave):
    for chave in range(2, max_chave + 1):  #Testa diferentes valores de chave
        texto_decifrado = transposicao(txt_cifrado, chave)
        print(f"Chave {chave}: {texto_decifrado}")  #Imprime o texto decifrado para cada chave


