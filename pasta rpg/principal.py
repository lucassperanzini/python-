import ex

#Números indicados na história da criatura
habilidade= 7
energia = 16



print('''       Bem vindo ao CALABOUÇO DA MORTE!
    
       Nessa aventura em um labirinto com diversas criaturas, testaremos você até o limite!
       Desafios estão a sua espera!
        
            \n''')

aceita_desafio = input('Você quer desafiar a morte? ').lower()


if aceita_desafio =='sim':

    CriaPersonagem = ex.CriarPersonagem()

    Criatura = ex.criarCriatura(habilidade,energia)

    Combate = ex.Combate()


else:
    print('Fracassado!! está com medinho?')