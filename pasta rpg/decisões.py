import historia
import funções
import jogaDADOS
import arte
import json

dado=0
opção_incorreta = print('opção incorreta, você perdeu!')

#### Decisões não feitas ainda (em aberto): 396, 186, 329, 135, 30, 212, 271, 176, 384


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

    SobreviveuPerdaEnergia = funções.PerdeEnergia(2)

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

    
    ComparaHabilidade = funções.ComparaHabilidade()
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

    ComparaHabilidade = funções.ComparaHabilidade()

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

    PerdeEnergia = funções.PerdeEnergia(4)

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


def decisao_91():
    H91 = historia.item_91()

    PerdeHabilidade = funções.PerdeHabilidade(4)


    #info do monstro 1
    nomeMonstro = 'ORCA'
    habilidade = 5
    energia = 5

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu o primeiro ORCA!!')
        print('Agora enfrenará o segundo ORCA!')

        #info do monstro 2
        nomeMonstro2 = 'ORCA2'
        habilidade2 = 6
        energia2 = 4

        CriaCriatura = funções.criarCriatura(habilidade2,energia2,nomeMonstro2)
        Combate1 = funções.Combate(nomeMonstro2)

        if Combate1:
            print('Você venceu os dois ORCA! Vá para 257')
            decisao_257()

        else:
            print(' Você perdeu o segundo combate! Você morreu!')
            arte.GameOver()
    else:
        print('Você perdeu o primeiro combate! Você Morreu!')
        arte.GameOver()

def decisao_257():
    H257 = historia.item_257()

    input('Volte para 164')

    decisao_164()


def decisao_164():
    H164 = historia.item_164()

    decisao = int(input('decisao :'))

    if decisao == 299:
        decisao_299()

    elif decisao == 83:
        decisao_83()
      
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_83():
    H83 = historia.item_83()

    input('Volte para 37')

    decisao_37()


def decisao_299():
    H299 = historia.item_299()

    decisao = int(input('decisao :'))

    if decisao == 126:
        decisao_126()

    elif decisao == 41:
        decisao_41()

    elif decisao == 83:
        decisao_83()
      
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_126():
    H126 = historia.item_126()

    
    decisao = int(input('decisao :'))

    if decisao == 226:
        decisao_226()

    elif decisao == 41:
        decisao_41()

    elif decisao == 83:
        decisao_83()
      
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_226():
    H226 = historia.item_226()

    GanhaEnergia = funções.GanhaStatus(3,'energia')

    decisao = int(input('decisao :'))

    if decisao == 41:
        decisao_41()

    elif decisao == 83:
        decisao_83()
      
    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_41():
    H41 = historia.item_41()

    decisao = int(input('decisao :'))

    if decisao == 98:
        decisao_98()

    elif decisao == 126:
        decisao_126()

    elif decisao == 83:
        decisao_83()
      
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_98():
    H98 = historia.item_98()

    testeSorte = funções.Sorte()

    if testeSorte:
        input('Vá para 105')
        decisao_105()
    else:
        input('Vá para 160')
        decisao_235()



def decisao_105():
    H105 = historia.item_105()

    decisao = int(input('decisao :'))

    if decisao == 126:
        decisao_126()

    elif decisao == 83:
        decisao_83()
      
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_235():
    H235 = historia.item_235()

    SobreviveuPerdaEnergia = funções.PerdeEnergia(2)

    if SobreviveuPerdaEnergia:
        decisao_73()
    else:
        arte.GameOver()


def decisao_73():
    H73 = historia.item_73()

    decisao = int(input('decisao :'))

    if decisao == 126:
        decisao_126()

    elif decisao == 83:
        decisao_83()
      
    else:
        print(opção_incorreta)
        arte.GameOver()






def decisao_135():
    H135 = historia.item_135()

    input('Volte para 68')

    decisao_68()


def decisao_189():
    H189 = historia.item_189()

    SobreviveuPerdaEnergia = funções.PerdeEnergia(3)

    if SobreviveuPerdaEnergia:

        #info do monstro 1
        nomeMonstro = 'ORCA'
        habilidade = 5
        energia = 5

        CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
        Combate = funções.Combate(nomeMonstro)

        if Combate:
            print('Você venceu o primeiro ORCA!!')
            print('Agora enfrenará o segundo ORCA!')

            #info do monstro 2
            nomeMonstro2 = 'ORCA2'
            habilidade2 = 6
            energia2 = 4

            CriaCriatura = funções.criarCriatura(habilidade2,energia2,nomeMonstro2)
            Combate1 = funções.Combate(nomeMonstro2)

            if Combate1:
                print('Você venceu os dois ORCA! Vá para 257')
                decisao_257()

            else:
                print(' Você perdeu o segundo combate! Você morreu!')
                arte.GameOver()
        else:
            print('Você perdeu o primeiro combate! Você Morreu!')
            arte.GameOver()

    else:
        arte.GameOver()


    
def decisao_380():
    H380 = historia.item_380()

    #info do monstro 1
    nomeMonstro = 'ORCA'
    habilidade = 5
    energia = 5

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu o primeiro ORCA!!')
        print('Agora enfrenará o segundo ORCA!')

        #info do monstro 2
        nomeMonstro2 = 'ORCA2'
        habilidade2 = 6
        energia2 = 4

        CriaCriatura = funções.criarCriatura(habilidade2,energia2,nomeMonstro2)
        Combate1 = funções.Combate(nomeMonstro2)

        if Combate1:
            print('Você venceu os dois ORCA! Vá para 257')
            decisao_257()

        else:
            print(' Você perdeu o segundo combate! Você morreu!')
            arte.GameOver()
    else:
        print('Você perdeu o primeiro combate! Você Morreu!')
        arte.GameOver()

  
def decisao_72():
    H72 = historia.item_72()

    PerdeHabilidade = funções.PerdeHabilidade(2)

    energia = habilidade = 'DESCONHECIDA'
    nomeMonstro = 'Demonio do Espelho'

    funções.criarCriatura(habilidade,energia,nomeMonstro)

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

    elif decisao == 384:
        decisao_384()
      
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_176():
    H176 = historia.item_176()

    input('Vá para 277')

    decisao_277()


def decisao_384():
    H384 = historia.item_384()

    SobreviveuPerdaEnergia = funções.PerdeEnergia(2)

    if SobreviveuPerdaEnergia:
        input('Volte para 277')
        decisao_277()
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_277():
    H277 = historia.item_277()

    input('Vá para 338')

    decisao_338()


def decisao_338():
    H338 = historia.item_338()

    decisao = int(input('decisao :'))

    if decisao == 123:
        decisao_123()

    elif decisao == 282:
        decisao_282()
      
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_123():
    H123 = historia.item_123()

    funções.GanhaStatus(1,'habilidade')

    funções.GanhaStatus(1,'energia')

    input('Vá para 282')

    decisao_282()
    


def decisao_282():
    H282 = historia.item_282()

    decisao = int(input('decisao :'))

    if decisao == 22:
        decisao_22()

    elif decisao == 388:
        decisao_388()
      
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_22():
    H22 = historia.item_22()

    decisao = int(input('decisao :'))

    if decisao == 63:
        decisao_63()

    elif decisao == 184:
        decisao_184()

    elif decisao == 311:
        decisao_311()
      
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_63():
    H63 = historia.item_63()

    input('Vá para 194')

    decisao_194()

def decisao_184():
    H184 = historia.item_184()

    decisao = int(input('decisao :'))

    if decisao == 323:
        decisao_323()

    elif decisao == 149:
        decisao_149()

      
    else:
        print(opção_incorreta)
        arte.GameOver()




def decisao_323():
    H323 = historia.item_323()

    input('Volte para 194')

    decisao_194()



def decisao_149():
    H149 = historia.item_149()

    energia = habilidade = 'DESCONHECIDA'
    nomeMonstro = 'BARBARO'

    funções.criarCriatura(habilidade,energia,nomeMonstro)

    testeSorte = funções.Sorte()

    if testeSorte:
        input('Vá para 70')
        decisao_70()
    else:
        input('Vá para 160')
        decisao_353()




def decisao_70():
    H70 = historia.item_70()

    arte.GameOver()



def decisao_353():
    H70 = historia.item_353()

    PerdaHabilidade = funções.PerdeHabilidade(1)

    SobreviveuPerdaEnergia = funções.PerdeEnergia(4)

    if SobreviveuPerdaEnergia:
        input('Vá para 325')
        decisao_325()
    else:
        arte.GameOver()







def decisao_311():
    H311 = historia.item_311()

    input('Vá para 325')

    decisao_325()


def decisao_325():
    H311 = historia.item_325()

    arte.GameOver

    

def decisao_194():
    H194 = historia.item_194()

    decisao = int(input('decisao :'))

    if decisao == 52:
        decisao_52()

    elif decisao == 138:
        decisao_138()

    elif decisao == 311:
        decisao_369()
      
    else:
        print(opção_incorreta)
        arte.GameOver()





def decisao_52():
    H52 = historia.item_52()

    energia = habilidade = 'DESCONHECIDA'
    nomeMonstro = 'BESTA SANGRENTA'
    funções.criarCriatura(habilidade,energia,nomeMonstro)

    decisao = int(input('decisao :'))

    if decisao == 138:
        decisao_138()

    elif decisao == 369:
        decisao_369()

    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_138():
    H138 = historia.item_138()

    decisao = int(input('decisao :'))

    if decisao == 397:
        decisao_397()

    elif decisao ==  75:
        decisao_75()

    elif decisao == 52:
        decisao_52()

    elif decisao == 369:
        decisao_369()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_369():
    H369 = historia.item_369()

    energia = 11
    habilidade = 10
    nomeMonstro = 'TROLL DA CAVERNA'

    funções.criarCriatura(habilidade,energia,nomeMonstro)

    SobreviveuCombate = funções.Combate(nomeMonstro)

    if SobreviveuCombate:
        print('Você venceu')
        input('Vote para 288')
        decisao_288()
    else:
        arte.GameOver()

def  decisao_288():
    H288 = historia.item_288()

    decisao = int(input('decisao :'))

    if decisao == 64:
        decisao_64()

    elif decisao ==  221:
        decisao_221()

    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_388():
    H388 = historia.item_388()

    decisao = int(input('decisao :'))

    if decisao == 23:
        decisao_23()

    elif decisao == 154:
        decisao_154()
      
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_23():
    H23 = historia.item_23()

    input('Vá para 154')

    decisao_154()


def decisao_154():
    H154 = historia.item_22()

    input('Volte para 22')

    decisao_22()


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

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

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
       decisao_336()
            
        
    elif decisao == 298:
        decisao_298()
            
    else:
        print(opção_incorreta)
        arte.GameOver()
    

def decisao_336():

    H336 = historia.item_336()

    PerdeHabilidade  = funções.PerdeHabilidade(4)

    energia = habilidade = "DESCONHECIDA"

    funções.criarCriatura(energia,habilidade,'Bruxa')

    input('Volte para 298')

    decisao_298()


def decisao_298():
    H298= historia.item_298()

    decisao = int(input('decisao :'))

    if decisao == 304:
       decisao_304()
            
        
    elif decisao == 279:
        decisao_279()
            
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_304():
    H304 = historia.item_304()

    SobreviveuPerdaEnergia = funções.PerdeEnergia(6)

    if SobreviveuPerdaEnergia:
        decisao_20()
    else:
        arte.GameOver()

def decisao_20():
    H20 = historia.item_20()

    PerdeHabilidade = funções.PerdeHabilidade(1)

    input('Siga para 279')

    decisao_279()



def decisao_279():
    H279 = historia.item_279()

    input('Volte para 32')

    decisao_32()

def decisao_130():
    H130 = historia.item_130()

    #info do monstro 1
    nomeMonstro = 'HOBGOBLIN'
    habilidade = 7
    energia = 5

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu o primeiro HOBGOBLIN!!')
        print('Agora enfrenará o segundo HOBGOBLIN!')

        #info do monstro 2
        nomeMonstro1 = 'HOBGOBLIN'
        habilidade1 = 6
        energia1 = 5

        CriaCriatura = funções.criarCriatura(habilidade1,energia1,nomeMonstro1)
        Combate1 = funções.Combate(nomeMonstro1)

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
    ComparaHabilidade = funções.ComparaHabilidade()

    if ComparaHabilidade:
        print("Vá para 80")
        decisao_80()
    
    else:
        print("Vá para 246")
        #Feito
        decisao_246()
    
    
def decisao_246():
    H246 = historia.item_246()

    PerdeSorte = funções.PerdeSorte(2)

    SobreviveuFarpas = funções.farpasMenosEnergia()

    if SobreviveuFarpas:
        print('Você sobreviveu!')
        decisao_313()
    else:
        print('As farpas foram letais, VOCÊ PERDEU')
        arte.GameOver()



def decisao_223():
    H223 = historia.item_223()


    PerdeSorte = funções.PerdeSorte(2)

    SobreviveuFarpas = funções.farpasMenosEnergia()

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

    PerdeHabilidade = funções.PerdeHabilidade(1)
    SobreviveuPerdeEnergia = funções.PerdeEnergia(4)

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

    H239 = funções.item_239()

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

def decisao_251():
    H251 = historia.item_251()

    input('Aperte ENTER para seguir para 344')

    decisao_344()



def decisao_133():
    H133 = historia.item_133()

    ComparaHabilidade = funções.ComparaHabilidade()

    if ComparaHabilidade:
        print("Vá para 178")
        decisao_178()
    
    else:
        print("Vá para 17")
        decisao_17()


def decisao_178():
    H178 = historia.item_178()

    input('Aperte ENTER para seguir para 344')

    decisao_344()


def decisao_17():
   H17 = historia.item_17()

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



def decisao_107():
    H107 = historia.item_107()

    decisao = int(input('decisão : '))

    if decisao == 168:
        decisao_168()
    
    elif decisao == 267:
        decisao_267()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_267():
    H267 = historia.item_267()

    decisao = int(input('decisão : '))

    if decisao == 352:
        decisao_352()
    
    elif decisao == 68:
        decisao_68()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_352():
    H352 = historia.item_352()

    decisao = int(input('decisão : '))

    if decisao == 254:
        decisao_254()
    
    elif decisao == 68:
        decisao_68()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_68():
    H68 = historia.item_68()

    decisao = int(input('decisão : '))

    if decisao == 271:
        decisao_271()
    
    elif decisao == 30:
        decisao_30()
    
    elif decisao == 212:
        decisao_212()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_30():
    H30 = historia.item_30()

    testeSorte = funções.Sorte()

    if testeSorte:
        input('Vá para 160')
        decisao_160()
    else:
        input('Vá para 160')
        decisao_319()



def decisao_212():
    H212 = historia.item_212()

    input('Va para 285')

    decisao_285()


def decisao_254():
    H254 = historia.item_254()

    #informações do Monstro
    nomeMonstro = 'VERME DA ROCHA'
    habilidade = 7
    energia = 11

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    ### Pode fugir para 117 após duas séries de ataque

    if Combate:
        print('Você venceu!!')
        decisao_76()
    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()


def decisao_76():
    H76 = historia.item_76()

    decisao = int(input('decisão : '))

    if decisao == 317:
        decisao_317()
    
    elif decisao == 117:
        decisao_117()
    
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_117():
    H117 = historia.item_117()

    decisao = int(input('decisão : '))

    if decisao == 329:
        decisao_329()
    
    elif decisao == 135:
        decisao_135()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_317():
    H317 = historia.item_317()

    energia = habilidade = 'DESCONHECIDA'
    nomeMonstro = 'VERME DA ROCHA'

    funções.criarCriatura(habilidade,energia,nomeMonstro)

    arte.GameOver()



def decisao_168():
    H168 = historia.item_168()

    decisao = int(input('decisão : '))

    if decisao == 94:
        decisao_94()
    
    elif decisao == 267:
        decisao_267()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_94():
    H94 = historia.item_94()
    
    input('Aperte ENTER para seguir para 174')

    decisao_174()


def decisao_174():
    H174 = historia.item_174()

    Sorte = funções.Sorte()

    if Sorte:
        decisao_39()
    
    else:
        decisao_350()



def decisao_350():
    H350 = historia.item_350()

    PerdeEnergia = funções.PerdeEnergiaNoDado()

    if PerdeEnergia:
        decisao_39()
    
    else:
        arte.GameOver()


def decisao_39():
    H39 = historia.item_39()

    #informações do Monstro
    nomeMonstro = 'MOSCA GIGANTE'
    habilidade = 7
    energia = 8

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!!')
        decisao_111()
    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()

    ##### FUGA para 267 #####


def decisao_111():
    H111 = historia.item_111()

    input('Aperte ENTER para seguir para 267')

    decisao_267()


def decisao_229():
    H229 = historia.item_229()

    input('Aperte ENTER para seguir para 107')

    decisao_107()

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


def decisao_396():
    H396 =  historia.item_396()

    decisao = int(input('decisão : '))

    if decisao == 151:
        decisao_151()
    elif decisao == 134:
        decisao_134()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_151():
    H151 = historia.item_151()

    nomeMonstro = 'GUARDIAO VOADOR'
    habilidade = 7
    energia = 8

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print(f'Você venceu o primeiro {nomeMonstro}!!')
        print(f'Agora enfrenará o segundo {nomeMonstro}!')

        #info do monstro 2
        nomeMonstro1 = 'GUARDIAO VOADOR'
        habilidade1 = 6
        energia1 = 5

        CriaCriatura = funções.criarCriatura(habilidade1,energia1,nomeMonstro1)
        Combate1 = funções.Combate(nomeMonstro1)

        if Combate1:
            print(f'Você venceu os dois {nomeMonstro }! Vá para 240')
            input('va para 240')
            decisao_240()

        else:
            print(' Você perdeu o segundo combate! Você morreu!')
            arte.GameOver()
    else:
        print('Você perdeu o primeiro combate! Você Morreu!')
        arte.GameOver()

def decisao_240():
    H240 = historia.item_240()

    decisao = int(input('decisão : '))

    if decisao == 34:
        decisao_34()
    elif decisao == 89:
        decisao_89()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_34():
    H34 = historia.item_34()

    arte.GameOver()


def decisao_89():
    H89 = historia.item_89()

    testeSorte = funções.Sorte()

    if testeSorte:
        input('Vá para 54')
        decisao_54()
    else:
        input('Vá para 261')
        decisao_261()


def decisao_54():
    H54 = historia.item_54()

    input('Vá para 239')

    decisao_239()


def decisao_261():
    H261 = historia.item_261()

    input('Volte para 239')

    decisao_239()


def decisao_134():
    H134 = historia.item_134()

    decisao = int(input('decisão : '))

    if decisao == 222:
        decisao_222()
    elif decisao == 247:
        decisao_247()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_222():
    nomeMonstro = 'MANTECORA'
    habilidade = energia = 'DESCONHECIDA'

    funções.criarCriatura(habilidade,energia,nomeMonstro)

    decisao = int(input('decisão : '))

    if decisao == 196:
        decisao_196()
    elif decisao == 247:
        decisao_6()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_196():
    H196 = historia.item_196()

    nomeMonstro = 'MANTECORA'
    habilidade = 11
    energia = 11

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print(f'Você venceu a {nomeMonstro}!!')
    
    else:
        print('Você perdeu o combate! Você Morreu!')
        arte.GameOver()

def decisao_6():
    H6 = historia.item_6()

    SobreviveuPerdaEnergia = funções.PerdeEnergia(2)

    if SobreviveuPerdaEnergia:
        nomeMonstro = 'MANTECORA'
        habilidade = 11
        energia = 11

        CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
        Combate = funções.Combate(nomeMonstro)

        if Combate:
            print(f'Você venceu a {nomeMonstro}!!')
        
        else:
            print('Você perdeu o combate! Você Morreu!')
            arte.GameOver()
    else:
        print('Acabou sua energia! Você Morreu!')
        arte.GameOver()




def decisao_247():
    H247 = historia.item_247()

    SobreviveuPerdeEnergiaDado = funções.PerdeEnergiaNoDado(2)

    if SobreviveuPerdeEnergiaDado:

        nomeMonstro = 'MANTECORA'
        habilidade = 11
        energia = 11

        CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
        Combate = funções.Combate(nomeMonstro)

        if Combate:
            print(f'Você venceu a {nomeMonstro}!!')
        
        else:
            print('Você perdeu o combate! Você Morreu!')
            arte.GameOver()
    else:
        print('Acabou sua energia! Você Morreu!')
        arte.GameOver()

def decisao_186():
    H186 = historia.item_186()

    TesteSorte = funções.Sorte()

    if TesteSorte:
        input('Va para 260')
        decisao_260()
    else:
        input('va para 358')
        decisao_358()


def decisao_260():
    H260 = historia.item_260()

    decisao = int(input('decisão : '))

    if decisao == 166:
        decisao_166()
    elif decisao == 140:
        decisao_140()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_358():
    H358 = historia.item_358()

    SobreviveuPerdaEnergia = funções.PerdeEnergia(2)

    if SobreviveuPerdaEnergia:
        input('volte para 239')
        decisao_239()
    else:
        arte.GameOver()


def decisao_275():
    H275 = historia.item_275()

    #checagem de sorte

    if funções.Sorte():
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

  SobreviveuPerdaEnergia = funções.PerdeEnergia(3)


  if SobreviveuPerdaEnergia:
      Sorte = funções.Sorte()
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

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!')
        #feito
        decisao_9()
    else:
          print('Você perdeu o Combate!')
          arte.GameOver()
