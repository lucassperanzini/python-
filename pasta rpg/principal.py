import funções
import decisões
import arte





print(f'''       {print(arte.BemVindo())}
      
                Bem vindo ao CALABOUÇO DA MORTE!
    
       Nessa aventura em um labirinto com diversas criaturas, testaremos você até o limite!
       Desafios estão a sua espera!
      

        
            \n''')

aceita_desafio = input('Você quer desafiar a morte? ').lower()


if aceita_desafio =='sim':

    CriaPersonagem = funções.CriarPersonagem()

    decisões.decisao_387()

    

   
   




else:
    print('Fracassado!! está com medinho?')









    # CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)

    # Combate = funções.Combate(nomeMonstro)

    # Sorte = funções.Sorte()




