import ex
import historia





opção_incorreta = print('opção incorreta, você perdeu!')



print('''       Bem vindo ao CALABOUÇO DA MORTE!
    
       Nessa aventura em um labirinto com diversas criaturas, testaremos você até o limite!
       Desafios estão a sua espera!
        
            \n''')

aceita_desafio = input('Você quer desafiar a morte? ').lower()


if aceita_desafio =='sim':

    CriaPersonagem = ex.CriarPersonagem()

    H1 = historia.item_1()
    decisao = int(input('decisão :'))

    
    if decisao == 270:
        H270 = historia.item_270()
    elif decisao == 66:
        H66 = historia.item_66()
        decisao = int(input('decisao :'))

        if decisao == 293:
            H293 = historia.item_293()
            decisao = int(input('decisao :'))

            if decisao == 137:
                H137 = historia.item_137()
                decisao = int(input('decisao :'))

                if decisao == 220:
                    H220 = historia.item_220()
                elif decisao == 362:
                    H362 = historia.item_362()
                else:
                    opção_incorreta
            
            elif decisao == 387:
                H387 = historia.item_387()
                #informações do Monstro
                nomeMonstro = 'HOMEM DA CAVERNA'
                habilidade = 7
                energia = 7
                
                CriaCriatura = ex.criarCriatura(habilidade,energia,nomeMonstro)
                Combate = ex.Combate(nomeMonstro)

                if Combate:
                    print('Você venceu!!')
                    H114 = historia.item_114()
                else:
                    print('perdeu')
                

            else:
                opção_incorreta

        elif decisao == 119:
            H119 = historia.item_119()
        else:
            opção_incorreta
    else:
        opção_incorreta
    

    # CriaCriatura = ex.criarCriatura(habilidade,energia,nomeMonstro)

    # Combate = ex.Combate(nomeMonstro)

    # Sorte = ex.Sorte()


else:
    print('Fracassado!! está com medinho?')