import random
l = 5
c =5
m = []
soma = 0
index = 0

def funcCriarMatriz():
    for i in range(l):
        linha = []
        for j in range(c):
            num = random.randint(1,5)
            linha.append(num)
        m.append(linha)

        


def funcSomaLinha4(soma):

    linha4 = m[3]
    

    for num in linha4:
        soma += num

    print(f'{soma} quarta linha!')



def funcSomaColuna2(soma):


    for linha in m:
        soma += linha[1]

    print(f"{soma} : soma coluna 2")


def funcDiagonal(soma,index):
    for linha in m:
        soma += linha[index]
        index += 1

    print(f"{soma} : soma diagonal")


def funcDiagonalInversa(soma,index):
    for linha in m:
        soma += linha[index - 1]
        index -= 1

    print(f"{soma} : soma diagonal inversa")


def funcSomaTotal(soma):
    for linha in m:
        for j in linha:
            soma += j
    print(f"{soma} : soma total da matriz")



def funcSomaFormatoInverso():
    somaFinal = 0

    index = 1
    for linha in m:
        for j in linha[index:]:
            somaFinal += j     
        index += 1

    return somaFinal


def funcSomaFormato(index):
    somaFinal = 0


    for linha in m:
        if m[0] == linha:
            continue
        for j in linha[:index + 1]:
            somaFinal += j
            
        index += 1
            
    return somaFinal




funcCriarMatriz()

for linha in m:
    print(linha)



somaPiramideInversa = funcSomaFormatoInverso()

print(somaPiramideInversa , 'Soma escada inversa')


somaPiramide = funcSomaFormato(index)

print(somaPiramide)






# funcSomaLinha4(soma)
# funcSomaColuna2(soma)
# funcDiagonal(soma,index)
# funcDiagonalInversa(soma,l)
# funcSomaTotal(soma)


