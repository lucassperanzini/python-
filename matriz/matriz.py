l = 3
c = 2

m1 = []
m2 = []


def func_matriz(matriz):
    for i in range(l):
        linha = []
        for j in range(c):
            valor = int(input('me diga um valor'))
            linha.append(valor)
        matriz.append(linha)

    return matriz




matriz1 = func_matriz(m1)
print(matriz1)



# func_soma(matriz1)

matriz2 = func_matriz(m2)
print(matriz2)



soma_matrizes = []

for i in range(l):
    linha =[]
    for j in range(c):   
        valor_soma = matriz1[i][j] + matriz2[i][j]
        linha.append(valor_soma)
    soma_matrizes.append(linha)


print(soma_matrizes)


   
            

# func_soma(matriz2)




    







# for i in range(l):
#     linha = []
#     for j in range(c):
#         valor = int(input('me diga um valor'))
#         linha.append(valor)
#     m2.append(linha)