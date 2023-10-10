import ex
import historia

import json



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
                    H264 = historia.item_264()
                    
                    decisao = int(input('decisao : '))
                    
                    if decisao == 130:
                        H130 = historia.item_130()

                        #info do monstro 1
                        nomeMonstro = 'HOBGOBLIN'
                        habilidade = 7
                        energia = 5

                        CriaCriatura = ex.criarCriatura(habilidade,energia,nomeMonstro)
                        Combate = ex.Combate(nomeMonstro)

                        if Combate:
                            print('Você venceu o primeiro HOBGOBLIN!!')
                            print('Agora enfrenará o segundo HOBGOBLIN!')

                            #info do monstro 2
                            nomeMonstro1 = 'HOBGOBLIN'
                            habilidade1 = 6
                            energia1 = 5

                            CriaCriatura = ex.criarCriatura(habilidade1,energia1,nomeMonstro1)
                            Combate1 = ex.Combate(nomeMonstro1)

                            if Combate1:
                                print('Você venceu os dois HOBGOBLIN! Vá para 9')
                                H9 = historia.item_9()
                            else:
                                print('perdeu')

                        else:
                            print('perdeu')
                            

                    elif decisao == 51:
                        H51 = historia.item_51()
                       
                        #info do monstro 
                        nomeMonstro = 'HOBGOBLIN'
                        habilidade = 6
                        energia = 5

                        CriaCriatura = ex.criarCriatura(habilidade,energia,nomeMonstro)
                        Combate = ex.Combate(nomeMonstro)

                        if Combate:
                            print('Você venceu!')
                            H9 = historia.item_9()
                        else:
                            print('perdeu')
                            
                    elif decisao == 355:
                        H355 = historia.item_355()
                        H110 = historia.item_110()
                        
                        decisao = int(input('decisao : '))
                        
                        if decisao == 58:
                            H58 = historia.item_58()
                        elif decisao == 223:
                            H223 = historia.item_223()
                        else:
                            print(opção_incorreta)
                    else:
                        print(opção_incorreta)
                else:
                    print(opção_incorreta)
            
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

                    decisao = int(input('decisao : '))

                    if decisao == 336:
                        H336 = historia.item_336()

                        with open(ex.caminhoFolhaDeAventuraAtual,'r') as f:
                            StatusGerais = json.load(f) 
                    
                        #perde habilidade
                        habilidade = StatusGerais['FolhaDeAventura']['habilidade']

                        print('Habilidade anterior',habilidade)
                
                        habilidade -= 4

                        StatusGerais['FolhaDeAventura']['habilidade'] = habilidade

                        print('Habilidade atual',habilidade)

                        with open(ex.caminhoFolhaDeAventuraAtual,'w') as f:
                            json.dump(StatusGerais,f)

                        #Volta para 298 Está com erro!! ele volta pra função mas nao pro elif
                        H298 = historia.item_298()
                    

                
                    elif decisao == 298:
                        H298 = historia.item_298()
                        decisao = int(input('decisao : '))


                        if decisao == 304:
                            H304 = historia.item_304()
                            #Aranha -- -6 pontos de energia

                            with open(ex.caminhoFolhaDeAventuraAtual,'r') as f:
                                    StatusGerais = json.load(f) 
                    
                            #perde habilidade
                            energia = StatusGerais['FolhaDeAventura']['energia']

                            print('Energia anterior',energia)
                
                            energia -= 6

                            StatusGerais['FolhaDeAventura']['energia'] = energia

                            with open(ex.caminhoFolhaDeAventuraAtual,'w') as f:
                                json.dump(StatusGerais,f)

                            if energia <= 0:
                                print('Acabou sua energia! Você perdeu')
                            else:
                                print('energia atual',energia)

                               



                        elif decisao == 279:
                            H279 = historia.item_279()

                        

                    else:
                        print(opção_incorreta)
                
                else:
                    print('perdeu')
                

            else:
                print(opção_incorreta)

        elif decisao == 119:
            H119 = historia.item_119()
            decisao = int(input('decisao :'))

           
        else:
            print(opção_incorreta)
    else:
        print(opção_incorreta)
    

    # CriaCriatura = ex.criarCriatura(habilidade,energia,nomeMonstro)

    # Combate = ex.Combate(nomeMonstro)

    # Sorte = ex.Sorte()


else:
    print('Fracassado!! está com medinho?')