import historia
import ex

def decisao_1():
    H1 = historia.item_1()
    decisao = int(input('decisão :'))

    if decisao == 270:
        #AINDA N
        H270 = historia.item_270()
    elif decisao == 66:
        #FEITO
        H66 = historia.item_66()
        decisao_66()
    else:
        print(opção_incorreta)



def decisao_66():
    H66 = historia.item_66()
    decisao = int(input('decisao :'))

    if decisao == 293:
        #FEITO
        H293 = historia.item_293()
        decisao = int(input('decisao :'))

        if decisao == 137:
            #FEITO
            decisao_137()
        elif decisao == 387:
            decisao_387()
        else:
            print(opção_incorreta)

       
    elif decisao == 119:
        #AINDA N
        H119 = historia.item_119()
        decisao = int(input('decisao :'))

    else:
        print(opção_incorreta)



def decisao_137():

    H137 = historia.item_137()
    decisao = int(input('decisao :'))

    if decisao == 220:
        #AINDA N
        H220 = historia.item_220()
    elif decisao == 362:
        #feito
        H362 = historia.item_362()
        H264 = historia.item_264()

        if decisao == 130:
            #FEITO
            decisao_130()
        elif decisao == 51:
            #FEITO
            decisao_51()
        #AINDA N
        elif decisao == 9:
            decisao_9()
      
        else:
            print(opção_incorreta)


def decisao_387():
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
        decisao = int(input('decisao :'))

        if decisao == 336:
            H336 = historia.item_336()

            MaldicaoBruxa  = ex.MaldicaoBruxa()
            
            #Volta para 298 Está com erro!! ele volta pra função mas nao pro elif
        
        elif decisao == 298:
            H298 = historia.item_298()
            decisao = int(input('decisao : '))
            


        else:
            print(opção_incorreta)
    else:
        print('perdeu')


def decisao_130():
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
            #CONTINUACAO NAO FEITA
            H9 = historia.item_9()

        else:
            print('perdeu')


def decisao_51():
    H51 = historia.item_51()
    
    #info do monstro 
    nomeMonstro = 'HOBGOBLIN'
    habilidade = 6
    energia = 5

    CriaCriatura = ex.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = ex.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!')
        #AINDA N
        H9 = historia.item_9()
    else:
        print('perdeu')
