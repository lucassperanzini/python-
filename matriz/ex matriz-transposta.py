

def func(linha,coluna):
    matriz = []
    for i in range(linha):
        linha_array = []
        for j in range(coluna):
            valor = int(input('digite num'))
            linha_array.append(valor)
        matriz.append(linha_array)

    return matriz

def func_transposta(matriz):
    n_linha = len(matriz)
    n_colunas = len(matriz[0])

    transposta = []
       
    for j in range(n_colunas):
        nova_linha = [None] * n_linha
        transposta.append(nova_linha)

    for i in range(n_linha):
        for j in range(n_colunas):
            transposta[j][i] = matriz[i][j]

    return transposta



l = int(input(f'Digite número de linhas : '))

c = int(input(f'Digite número de colunas : '))




matriz = func(c,l)

print(matriz)

matriz_transposta = func_transposta(matriz)

print(matriz_transposta)



#nova matriz

#