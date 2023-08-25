l = 5
c = 3

m1 = []


for i in range(l):
    linha = []
    for j in range(c):
        num= int(input(f' {j + 1} valores :'))
        linha.append(num)
    m1.append(linha)

print(m1)


menor = m1[0][0]

posicao_i = 0
posicao_j = 0

for i in range(len(m1)):
    for j in range(len(m1[i])):
        if m1[i][j] < menor:
             menor = m1[i][j]
             posicao_i = i
             posicao_j = j

print(f' o menor número é {menor} na posicao {posicao_i} {posicao_j}')
