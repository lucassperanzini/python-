import random
import csv

lista_palavras = []

with open('D:/palavras.csv','r') as f:
    reader = csv.reader(f)

    for i in reader:
        lista_palavras += i
    print(lista_palavras)
    
escolha_palavra = random.choice(lista_palavras)
print(escolha_palavra)

jogador1 = input('qual é o seu nome?')
jogador2 = input('qual é o seu nome?')   
jogador3 = input('qual é o seu nome?')

nomes = {

    'jogador1':jogador1,'pontos':0, 
    'jogador2':jogador2,'pontos':0,  
    'jogador3':jogador3,'pontos':0,  
    
}

lista_valores = []

with open('D:/ValorRoda.txt','r') as f:
        for i in f:
            print(i)
            lista_valores.append(i)
        escolha_valor = random.choice(lista_valores)
    
      
while True:
    print(f'Dica da palavra : Começa com {escolha_palavra[0]} ')


    rodar = input(f'{nomes["jogador1"]} rode a roda!!')

    print(f'valor da roleta {escolha_valor}')

    if int(escolha_valor) != 0:
       letra = input('escolha uma letra : ')
       if letra in escolha_palavra:
           print(f'Parábens acertou uma letra! letras faltantes {len(escolha_palavra) - 1}')
           nomes['pontos'] += escolha_valor
           print(nomes)
           



