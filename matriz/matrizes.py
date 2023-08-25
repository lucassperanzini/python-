l = 5

c = 2

matriz = []

print('digite seu nome e valor!')
for i in range(l):
    linha = []
    for j in range(c):
       valor = input()
       linha.append(valor)

    matriz.append(linha)

print(matriz)


estado = input('qual estado você vive?')


for i in range(l):
    if matriz[i][1] == estado:
        print(f" nome {matriz[i][0]}")

