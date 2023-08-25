#0: -----
#1: .----
#2: ..---
#3: ...--
#4: ....-
#5: .....
#6: -....
#7: --...
#8: ---..
#9: ----.
#10: .-.-.

lista_morse = ["-----",".----","..---","...--","....-",".....","-....","--...","---..","----.",".-.-."]

numeros_inicias = input("me fale alguns números")   
numeros_iniciais = numeros_inicias.split(" ")

def code_morse(code):
    for i in lista_morse:
         for j in range(len(code)):
            if i == lista_morse[int(code[j])]:
                code[j] = str(lista_morse.index(i))
            return code

print|(numeros_iniciais)

code_morse(numeros_iniciais)






    
    




