import random
lista_jogadas = ["PEDRA","PAPEL","TESOURA"]

escolha_usuario = input("PEDRA PAPEL OU TESOURA?")

escolha_pc = random.randint(0,3)
escolha_pc = random.choice(lista_jogadas)


print(F" A escolha do oponnte foi {escolha_pc}")

if escolha_usuario == escolha_pc:
    print("Empate!!!")
elif escolha_usuario == "PEDRA" and escolha_pc == "TESOURA":
    print("Você venceu!")
elif escolha_usuario == "TESOURA" and escolha_pc == "PEDRA":
    print("PC ganhou!!")
elif escolha_usuario == "TESOURA" and escolha_pc == "PAPEL":
    print("Você venceu!")
elif escolha_usuario == "PAPEL" and escolha_pc == "TESOURA":
    print("PC ganhou!!")
elif escolha_usuario == "PAPEL" and escolha_pc == "PEDRA":
    print("Você venceu!")
elif escolha_usuario == "PEDRA" and escolha_pc == "PAPEL":
    print("PC ganhou!!")



