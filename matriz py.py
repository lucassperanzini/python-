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
            num = random.randint(10,30)
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
    somaLista = []
    somaFinal = 0

    index = 1
    for linha in m:
        somaLista.append(linha[index:])
        index += 1

    for i in somaLista:
        for j in i:
            somaFinal += j

    return somaFinal


def funcSomaFormato(soma,index):
    somaLista = []
    soma = 0

    for linha in m:
        if m[0] == linha:
            continue
        else:
            somaLista.append(linha[index:(index + 1)])
            print(somaLista)
            index += 1
            

    for i in somaLista:
        for j in i:
            soma += j

    return soma



    

funcCriarMatriz()

for linha in m:
    print(linha)


somaPiramideInversa = funcSomaFormatoInverso()

print(somaPiramideInversa , 'é isso')


somaPiramide = funcSomaFormato(soma,index)

print(somaPiramide)






# funcSomaLinha4(soma)
# funcSomaColuna2(soma)
# funcDiagonal(soma,index)
# funcDiagonalInversa(soma,l)
# funcSomaTotal(soma)


