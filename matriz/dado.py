matriz = [[0] * 10 for i in range(10)]

# Preenchendo a matriz com o resultado da multiplicação
for i in range(1, 11):
    for j in range(1, 11):
        matriz[i-1][j-1] = i * j

# Imprimindo a matriz
for i in range(10):
    for j in range(10):
        print(f'{matriz[i][j]:2}', end=' ')
    print()