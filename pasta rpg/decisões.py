import historia
import ex
import jogaDADOS
import json

opção_incorreta = print('opção incorreta, você perdeu!')


def decisao_1():
    H1 = historia.item_1()
    decisao = int(input('decisão :'))

    if decisao == 270:
        #FEITO
        decisao_270()

    elif decisao == 66:
        #FEITO
        decisao_66()

    else:
        print(opção_incorreta)



def decisao_66():
    H66 = historia.item_66()
    decisao = int(input('decisao :'))

    if decisao == 293:
        #FEITO
        decisao_293()
       
    elif decisao == 119:
        #AINDA N
        H119 = historia.item_119()


    else:
        print(opção_incorreta)



def decisao_270():
    H270 = historia.item_270()
    
    decisao_66()



def decisao_293():
    H293 = historia.item_293()
    decisao = int(input('decisao :'))

    if decisao == 137:
        #FEITO
        decisao_137()

    elif decisao == 387:
        decisao_387()

    else:
        print(opção_incorreta)


def decisao_119():
    H119 = historia.item_119()

    decisao = int(input('decisao :'))

    if decisao == 56:
        #não feito
        decisao_56()

    elif decisao == 293:
        #feito
        decisao_293()
    
    else:
        print(opção_incorreta)


def decisao_56():
    H56 = historia.item_56()




def decisao_137():
    H137 = historia.item_137()
    decisao = int(input('decisao :'))

    if decisao == 220:
        #AINDA N
        decisao_220()

    elif decisao == 362:
        #feito
        decisao_362()
      
    else:
        print(opção_incorreta)


def decisao_220():
    H220 = historia.item_220()
    decisao = int(input('decisao :'))

    if decisao == 61:
        decisao_61()

    
    elif decisao == 346:
        decisao_346()
    
    else:
        print(opção_incorreta)


def decisao_61():
    #F
    H61 = historia.item_61()

    print("Foi de comes e bebes")
    exit()


def decisao_346():
    H346 = historia.item_346()

    decisao_362()


def decisao_264():
    H264 = historia.item_264()
    decisao = int(input('decisao :'))

    if decisao == 130:
        decisao_130()

    elif decisao == 51:
        decisao_51()

    elif decisao == 355:
        decisao_355()

    else:
        print(opção_incorreta)


def decisao_355():
    H355 = historia.item_355()

    decisao_110()


def decisao_362():
    H362 = historia.item_362()

    decisao_264()


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
            decisao_9()

        else:
            print('perdeu')


def decisao_9():
    H9 = historia.item_9()
    decisao = int(input('decisao : '))

    if decisao == 158:
        decisao_158()
    
    elif decisao == 375:
        decisao_375()
    
    else:
        print(opção_incorreta)


def decisao_375():
    H375 = historia.item_375()
    
    decisao_110()


def decisao_110():
    H110 = historia.item_110()
    decisao = int(input('decisao : '))

    if decisao == 58:
        decisao_58()
    
    elif decisao == 223:
        #Não feito
        decisao_223()
    
    else:
        print(opção_incorreta)


def decisao_58():
    H58 = historia.item_58()
    
    #Compara: se soma dos dados <= habilidade vai para 80, senão vai para 246
    
    dado = 0
    dado1 = jogaDADOS.jogaDados(dado)
    dado2 = jogaDADOS.jogaDados(dado)

    dadoTotal = dado1 + dado2

    with open(ex.caminhoFolhaDeAventuraAtual,'r') as f:
        StatusGerais = json.load(f)
    
    habilidade = StatusGerais['FolhaDeAventura']['habilidade']

    if dadoTotal <= habilidade:
        print("Total dos dados menor ou igual a HABILIDADE, vá para 80")
        decisao_80()

    else:
        print("Total dos dados maior que HABILIDADE, vá para 246")
        #Não feito
        decisao_246()


def decisao_80():
    H80 = historia.item_80()
    #Não feito
    decisao_313()





def decisao_158():
    # PERDE 1 de habilidade e 4 de energia
    H158 = historia.item_158()

    ex.PerdeHabilidade(1)
    ex.PerdeEnergia(4)

    #se tiver energia vai para 275
    decisao_275()


def decisao_275():
    H275 = historia.item_275()

    #checagem de sorte

    if ex.Sorte():
        decisao_231()
    else:
        #Não feito
        decisao_309()


def decisao_231():
    H231 = historia.item_231()

    decisao_110()


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
        #feito
        decisao_9()
    else:
        print('perdeu')
