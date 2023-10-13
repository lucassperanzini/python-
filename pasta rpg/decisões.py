import historia
import ex
import jogaDADOS
import arte
import json

dado=0
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
        arte.GameOver()



def decisao_66():
    H66 = historia.item_66()
    decisao = int(input('decisao :'))

    if decisao == 293:
        #FEITO
        decisao_293()
       
    elif decisao == 119:
        #FEITO
        decisao_119()


    else:
        print(opção_incorreta)
        arte.GameOver()



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
        #FEITO
        decisao_387()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_119():
    H119 = historia.item_119()

    decisao = int(input('decisao :'))

    if decisao == 56:
        #feito
        decisao_56()

    elif decisao == 293:
        #feito
        decisao_293()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_56():
    H56 = historia.item_56()

    decisao = int(input('decisao :'))

    if decisao == 373:
        decisao_373()
    elif decisao == 215():
        decisao_215()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_373():
    H373 = historia.item_373()

    input('Aperte ENTER para seguir para 13')

    decisao_13()


def decisao_215():

    H215 = historia.item_215()

    SobreviveuPerdaEnergia = ex.PerdeEnergia(2)

    if SobreviveuPerdaEnergia:
        input('Aperte ENTER para seguir para 13')
        decisao_13()
    else:
        arte.GameOver()

def decisao_13():
    H13 = historia.item_13()

    decisao = int(input('decisão : '))

    if decisao == 141:
        decisao_141()
    elif decisao == 182:
        decisao_182()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_141():
    H141 = historia.item_141()

    
    ComparaHabilidade = ex.ComparaHabilidade()
    # Se habilidade for menor que a soma dos dados, sege 71 se nao segue 96
    if ComparaHabilidade:
        input('Siga para 72:')
        decisao_72()
    else:
        input('Siga para 96')
        decisao_96()


def decisao_182():
    H182 = historia.item_182()

    decisao = int(input('decisao :'))

    if decisao == 25:
        decisao_25()

    elif decisao == 242:
        decisao_242()
      
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_25():
    H25 = historia.item_25()
    input(' Aperte ENTER para seguir para 197')

    decisao_197()


def decisao_242():
    H242 = historia.item_242()

    ComparaHabilidade = ex.ComparaHabilidade()

    if ComparaHabilidade:
        input('Siga para 48')
        decisao_48()
    else:
        input('Siga para 366')
        decisao_366()

def decisao_48():
    H48 = historia.item_48()

    input('Siga para 197')

    decisao_197()

def decisao_366():

    H366 = historia.item_366()

    arte.GameOver()


def decisao_197():
    H197 = historia.item_197()

    decisao = int(input('decisao :'))

    if decisao == 171:
   
        decisao_171()

    elif decisao == 156:
      
        decisao_156()

    elif decisao == 326:
    
        decisao_326()
      
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_171():
    H171 = historia.item_171()

    PerdeEnergia = ex.PerdeEnergia(4)

    input('Siga para 326')

    decisao_326()


def decisao_156():
    H156 = historia.item_156()

    decisao = int(input('decisao :'))

    if decisao == 208:
   
        decisao_208()

    elif decisao == 326:
      
        decisao_326()
      
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_208():
    H208 = historia.item_208()

    input('Siga para 326')

    decisao_326()


def decisao_326():
    H326 = historia.item_326()
    
    ValorDado = jogaDADOS.jogaDados(dado)

    print(ValorDado)

    if ValorDado == 1 or ValorDado == 2:
        decisao_91()
    elif ValorDado == 3 or ValorDado == 4:
        decisao_189()
    elif ValorDado == 5 or ValorDado == 6:
        decisao_380()



def decisao_72():
    H72 = historia.item_72()

    PerdeHabilidade = ex.PerdeHabilidade(2)

    input('Vá para 122')

    decisao_122()


def decisao_96():
    H96 = historia.item_96()

    arte.GameOver()



def decisao_122():
    H122 = historia.item_122()

    decisao = int(input('decisao :'))

    if decisao == 176:
        decisao_176()

    elif decisao == 362:
        decisao_384()
      
    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_137():
    H137 = historia.item_137()
    decisao = int(input('decisao :'))

    if decisao == 220:
        #feito
        decisao_220()

    elif decisao == 362:
        #feito
        decisao_362()
      
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_220():
    H220 = historia.item_220()
    decisao = int(input('decisao :'))

    if decisao == 61:
        decisao_61()

    
    elif decisao == 346:
        decisao_346()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_61():
    #F
    H61 = historia.item_61()

    print("Foi de comes e bebes")
    arte.GameOver()


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
        arte.GameOver()


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
        decisao_114()
    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()


def decisao_114():
    H114 = historia.item_114()
    decisao = int(input('decisao :'))

    if decisao == 336:
        H336 = historia.item_336()

        PerdeHabilidade  = ex.PerdeHabilidade(4)
            
        decisao_220()
        
    elif decisao == 298:
        H298 = historia.item_298()
        decisao = int(input('decisao : '))
            
    else:
        print(opção_incorreta)
        arte.GameOver()
    


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
            print(' Você perdeu o segundo combate! Você morreu!')
            arte.GameOver()
    else:
        print('Você perdeu o primeiro combate! Você Morreu!')
        arte.GameOver()

def decisao_9():
    H9 = historia.item_9()
    decisao = int(input('decisao : '))

    if decisao == 158:
        decisao_158()
    
    elif decisao == 375:
        decisao_375()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_375():
    H375 = historia.item_375()
    
    decisao_110()


def decisao_110():
    H110 = historia.item_110()
    decisao = int(input('decisao : '))

    if decisao == 58:
        decisao_58()
    
    elif decisao == 223:
        decisao_223()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_58():
    H58 = historia.item_58()
    
    #Compara: se soma dos dados <= habilidade vai para 80, senão vai para 246
    #Corrigir função
    
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

def decisao_246():
    H246 = historia.item_246()

    PerdeSorte = ex.PerdeSorte(2)

    SobreviveuFarpas = ex.farpasMenosEnergia()

    if SobreviveuFarpas:
        print('Você sobreviveu!')
        decisao_313()
    else:
        print('As farpas foram letais, VOCÊ PERDEU')
        arte.GameOver()



def decisao_223():
    H223 = historia.item_223()


    PerdeSorte = ex.PerdeSorte(2)

    SobreviveuFarpas = ex.farpasMenosEnergia()

    if SobreviveuFarpas:
        print('Você sobreviveu!')
        decisao_313()
    else:
        print('Acabou sua energia!')
        arte.GameOver()

def decisao_313():
    H313 =  historia.item_313()

    input('Aperte ENTER para seguir para 32')

    decisao_32()
  
def decisao_80():
    H80 = historia.item_80()

    decisao_313()





def decisao_158():
    # PERDE 1 de habilidade e 4 de energia
    H158 = historia.item_158()

    PerdeHabilidade = ex.PerdeHabilidade(1)
    SobreviveuPerdeEnergia = ex.PerdeEnergia(4)

    if SobreviveuPerdeEnergia:
        #se tiver energia vai para 275
        decisao_275()
    else:
        print('Acabou sua Energia!')
        arte.GameOver()

def decisao_32():
    H32 = historia.item_32()

    input('Aperte ENTER para seguir para 37')

    decisao_37()



def decisao_37():
    H37 = historia.item_37()

    decisao = int(input('decisao :'))

    if decisao == 239:
        decisao_239()
    elif decisao == 351:
        decisao_351()
    else:
        print(opção_incorreta)


def decisao_239():

    H239 = ex.item_239()

    decisao = int(input('decisão : '))

    if decisao == 102:
        decisao_102()

    elif decisao == 344:
        decisao_344()
    
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_102():

    H102 = historia.item_102()

    decisao = int(input('decisão : '))

    if decisao == 133:
        decisao_133()
    elif decisao == 251:
        decisao_251()
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_344():
    H344 = historia.item_344()

    decisao = int(input('decisão : '))

    if decisao == 229:
        decisao_229()
    elif decisao == 107:
        decisao_107()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_351():
    H351 = historia.item_351()

    decisao = int(input('decisão : '))

    if decisao == 396:
        decisao_396()
    elif decisao == 186:
        decisao_186()
    else:
        print(opção_incorreta)
        arte.GameOver()

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

    input('Aperte ENTER para seguir para 110')

    decisao_110()


def decisao_309():
  H309 = historia.item_309()

  SobreviveuPerdaEnergia = ex.PerdeEnergia(3)


  if SobreviveuPerdaEnergia:
      Sorte = ex.Sorte()
      print('----------------------------------------------')
      if Sorte:
          print('Você foi redirecionado para 231!')
          decisao_231()
      else:
          print('Você foi redirecionado para 193!')
          decisao_193()
  else:
    print('Acabou sua energia!')
    arte.GameOver()
      


def decisao_193():
    H193  = historia.item_193()

    arte.GameOver()



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
          print('Você perdeu o Combate!')
          arte.GameOver()
