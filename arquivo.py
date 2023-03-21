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

codigo_morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-."
}

numeros_inicias = input("me fale alguns números")   
numeros_iniciais = numeros_inicias.split(" ")

def code_morse(codes):
    for code in codes:
        print(codigo_morse[code], end=" ")
  



code_morse(numeros_iniciais)






    
    




