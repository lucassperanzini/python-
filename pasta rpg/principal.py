import ex

#Números indicados na história da criatura
habilidade= 12
energia = 22

nomeMonstro = 'Alfredo'



print('''       Bem vindo ao CALABOUÇO DA MORTE!
    
       Nessa aventura em um labirinto com diversas criaturas, testaremos você até o limite!
       Desafios estão a sua espera!
        
            \n''')

aceita_desafio = input('Você quer desafiar a morte? ').lower()


if aceita_desafio =='sim':
    
    CriaPersonagem = ex.CriarPersonagem()

    CriaCriatura = ex.criarCriatura(habilidade,energia,nomeMonstro)

    Combate = ex.Combate(nomeMonstro)

    Sorte = ex.Sorte()


else:
    print('Fracassado!! está com medinho?')