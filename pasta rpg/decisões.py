import historia
import funções
import jogaDADOS
import arte
import json

dado=0
opção_incorreta ='opção inválida, você perdeu!'

escolha_171_feita = escolha_251_feita = escolha_330_feita = escolha_269_feita = escolha_389_feita = escolha_367_feita = escolha_345_feita = escolha_257_feita = escolha_162_feita = escolha_201_feita = escolha_75_feita = escolha_94_feita = False


## decisões 124, 143


def decisao_1():
    H1 = historia.item_1()
    decisao = int(input('decisão :'))

    if decisao == 270:
        decisao_270()

    elif decisao == 66:
        decisao_66()

    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_66():
    H66 = historia.item_66()
    decisao = int(input('decisao :'))

    if decisao == 293:
        
        decisao_293()
       
    elif decisao == 119:
        decisao_119()


    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_147():
    H147 = historia.item_147()

    funções.GanhaStatus(1,'energia','⚡')

    input("Vá para 182")
    decisao_182()

def decisao_270():
    H270 = historia.item_270()
    
    decisao_66()



def decisao_293():
    H293 = historia.item_293()
    decisao = int(input('decisao :'))

    if decisao == 137:
        decisao_137()

    elif decisao == 387:
        decisao_387()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_119():
    H119 = historia.item_119()

    decisao = int(input('decisao :'))

    if decisao == 56:
        decisao_56()

    elif decisao == 293:
        decisao_293()
    
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_56():
    H56 = historia.item_56()

    decisao = int(input('decisao :'))

    if decisao == 373:
        decisao_373()
    elif decisao == 215:
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

    funções.PerdeEnergia(2)

    
    input('Aperte ENTER para seguir para 13')
    decisao_13()
    

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
    # Se habilidade for menor que a soma dos dados, sege 72 se nao segue 96
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

    global escolha_171_feita
    escolha_171_feita = True

    funções.PerdeEnergia(4)

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

    global escolha_257_feita
    escolha_257_feita = True

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

    GanhaEnergia = funções.GanhaStatus(3,'energia','⚡')

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

    funções.PerdeEnergia(2)

    input('Siga para 73')
    decisao_73()
  


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

    funções.PerdeEnergia(3)



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

    funções.PerdeEnergia(2)

    input('Volte para 277')
    decisao_277()
    

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

    funções.GanhaStatus(1,'habilidade','👊')

    funções.GanhaStatus(1,'energia','⚡')

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

    funções.PerdeEnergia(4)
    
    input('Vá para 325')
    decisao_325()
   





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


def decisao_397():
    H397 = historia.item_397()

    funções.GanhaStatus(2,'sorte','🍀')

    decisao = int(input('decisao :'))

    if decisao == 52:
        decisao_52()

    elif decisao ==  369:
        decisao_369()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_75():
    H75 = historia.item_75()

    funções.GanhaStatus(2,'sorte','🍀')

    decisao = int(input('decisao :'))

    if decisao == 52:
        decisao_52()

    elif decisao ==  369:
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

def decisao_221():
    H221 = historia.item_221()

    decisao = int(input('decisao :'))

    if decisao == 374:
        decisao_374()

    elif decisao ==  60:
        decisao_60()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_374():
    H374 = historia.item_374()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 118")
        decisao_118()
    
    else:
        input("Vá para 295")
        decisao_295()


def decisao_295():
    H295 = historia.item_295()

    perdeenergia = funções.PerdeEnergia(5)

    if perdeenergia:
        decisao_206()


def decisao_206():
    H206 = historia.item_206()

    ## Usa Provisões

    decisao_60()



def decisao_118():
    H118 = historia.item_118()

    decisao_60()


def decisao_60():
    H60 = historia.item_60()

    decisao = int(input('decisao :'))

    if decisao == 365:
        decisao_365()

    elif decisao ==  179:
        decisao_179()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_179():
    H179 = historia.item_179()

    funções.PerdeEnergia(2)

    decisao = int(input('decisao :'))

    if decisao == 290:
        decisao_290()

    elif decisao == 191:
        decisao_191()

    elif decisao == 84:
        decisao_84()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_84():
    H84 = historia.item_84()

    valorDado = jogaDADOS.jogaDados(dado)
    valorDado2 = jogaDADOS.jogaDados(dado)

    total = valorDado + valorDado2

    print(valorDado, valorDado2)

    if total > 8:
        decisao_152()

    elif total <= 8:
        decisao_121()



def decisao_290():
    H290 = historia.item_290()

    valorDado = jogaDADOS.jogaDados(dado)
    valorDado2 = jogaDADOS.jogaDados(dado)

    total = valorDado + valorDado2

    print(valorDado, valorDado2)

    if total == 8:
        decisao_152()

    elif total < 8 or total > 8:
        decisao_121()



def decisao_191():
    H191 = historia.item_191()

    valorDado = jogaDADOS.jogaDados(dado)
    valorDado2 = jogaDADOS.jogaDados(dado)

    total = valorDado + valorDado2

    print(valorDado, valorDado2)

    if total < 8:
        decisao_152()
    elif total >= 8:
        decisao_121()


def decisao_152():
    H152 = historia.item_152()

    ComparaHab = funções.ComparaHabilidade()

    if ComparaHab:
        input("Vá para 55")
        decisao_55()
    
    else:
        input("Vá para 202")
        decisao_202()


def decisao_202():
    H202 = historia.item_202()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 18")
        decisao_18()
    
    else:
        input("Vá para 42")
        decisao_42()


def decisao_18():
    H18 = historia.item_18()

    comparaHab = funções.ComparaHabilidade()

    if comparaHab:
        input("Vá para 55")
        decisao_55()
    
    else:
        input("Vá para 202")
        decisao_202()

def decisao_42():
    H42 = historia.item_42()

    funções.PerdeEnergia(5)

    comparaHab = funções.ComparaHabilidade()

    if comparaHab:
        input("Vá para 55")
        decisao_55()
    
    else:
        input("Vá para 202")
        decisao_202()



def decisao_55():
    H55 = historia.item_55()

    decisao = int(input('decisao :'))

    if decisao == 143:
        decisao_143()

    elif decisao == 347:
        decisao_347()

    elif decisao == 40:
        decisao_40()

    else:
        print(opção_incorreta)
        arte.GameOver()





def decisao_347():
    H347 = historia.item_347()

    arte.GameOver()


# def decisao_143():
#     H143 = historia.item_143()

##### DÚVIDA Combate duplo contra 1 escorpião gigante


def decisao_2():
    H2 = historia.item_2()

    arte.GameOver()


def decisao_40():
    H40 = historia.item_40()

    #informações do Monstro
    nomeMonstro = 'MINOTAURO'
    habilidade = 9
    energia = 9

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!!')
        decisao_163()
    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()


def decisao_163():
    H163 = historia.item_163()

    decisao = int(input('decisao :'))

    if decisao == 363:
        decisao_363()

    elif decisao == 302:
        decisao_302()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_363():
    H363 = historia.item_363()

    funções.GanhaStatus(2,'energia','⚡')

    input("Vá para 302")
    decisao_302()


def decisao_302():
    H302 = historia.item_302()

    #informações do Monstro
    nomeMonstro = 'THROM'
    habilidade = 10
    energia = 12

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!!')
        decisao_379()
    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()


def decisao_379():
    H379 = historia.item_379()

    decisao = int(input('decisao :'))

    if decisao == 213:
        decisao_213()

    elif decisao == 145:
        decisao_145()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_145():
    H145 = historia.item_145()

    ### Reduzir força de ataque em 2 a cada série

    #informações do Monstro
    nomeMonstro = 'ANÃO'
    habilidade = 8
    energia = 6

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!!')
        decisao_28()
    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()

def decisao_28():
    H28 = historia.item_18()

    funções.GanhaStatus(1,'habilidade','👊')

    input("Vá para 213")
    decisao_213()



def decisao_213():
    H213 = historia.item_213()

    decisao = int(input('decisao :'))

    if decisao == 108:
        decisao_108()

    elif decisao == 14:
        decisao_14()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_14():
    H14 = historia.item_14()
    
    decisao = int(input('decisao :'))

    if decisao == 157:
        decisao_157()

    elif decisao == 310:
        decisao_310()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_310():
    H310 = historia.item_310()

    decisao = int(input('decisao :'))

    if decisao == 339:
        decisao_339()

    elif decisao == 262:
        decisao_262()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_262():
    H262 = historia.item_262()

    decisao = int(input('decisao :'))

    if decisao == 337:
        decisao_337()

    elif decisao == 173:
        decisao_173()
    
    elif decisao == 368:
        decisao_368()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_337():
    H337 = historia.item_337()

    funções.GanhaStatus(1,'energia','⚡')
    funções.PerdeSorte(2)

    decisao = int(input('decisao :'))

    if decisao == 173:
        decisao_173()

    elif decisao == 368:
        decisao_368()

    else:
        print(opção_incorreta)
        arte.GameOver()
        


def decisao_173():
    H173 = historia.item_173()

    decisao = int(input('decisao :'))

    if decisao == 337:
        decisao_337()

    elif decisao == 368:
        decisao_368()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_368():
    H368 = historia.item_368()

    decisao = int(input('decisao :'))

    if decisao == 165:
        decisao_165()

    elif decisao == 234:
        decisao_234()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_165():
    ######### REVER
    H165 = historia.item_165()

    input('Vá para 234')

    decisao_234()



def decisao_234():
    H234 = historia.item_234()

    decisao = int(input('decisao :'))

    if decisao == 183:
        decisao_183()

    elif decisao == 207:
        decisao_207()

    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_183():
    H183 = historia.item_183()

    decisao = int(input('decisao :'))

    if decisao == 386:
        decisao_386()

    elif decisao == 218:
        decisao_218()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_207():
    H207 = historia.item_207()

    funções.PerdeEnergia(3)

    decisao = int(input('decisao :'))

    if decisao == 386:
        decisao_386()

    elif decisao == 218:
        decisao_218()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_386():
    H386 = historia.item_386()

    funções.PerdeEnergia(1)

    input('Volte para 218')

    decisao_218()


def decisao_218():
    H218 = historia.item_218()

    decisao = int(input('decisao :'))

    if decisao == 65:
        decisao_65()

    elif decisao == 252:
        decisao_252()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_65():
    H218 = historia.item_65()

    decisao = int(input('decisao :'))

    if decisao == 345:
        decisao_345()

    elif decisao == 372:
        decisao_372()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_345():
    H345 = historia.item_345()

    global escolha_345_feita
    escolha_345_feita = True

    input('Volte para 252')

    decisao_252()


def decisao_372():
    H372 = historia.item_372()

    arte.GameOver()
       
       

def decisao_252():
    H252 = historia.item_252()

    input('Volte para 90')

    decisao_90()


def decisao_90():
    H90 = historia.item_90()

    decisao = int(input('decisao :'))

    if decisao == 172:
        decisao_172()

    elif decisao == 357:
        decisao_357()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_172():
    H90 = historia.item_172()

    #informações do Monstro
    nomeMonstro = 'BESTA SANGRENTA'
    habilidade = 9
    energia = 8

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!!')
        decisao_278()
    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()

def decisao_357():
    H357 = historia.item_357()

    decisao = int(input('decisao :'))

    if decisao == 255:
        decisao_255()

    elif decisao == 332:
        decisao_332()

    elif decisao == 180:
        decisao_180()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_255():
    H255 = historia.item_255()

    arte.GameOver()


def decisao_332():
    H332 = historia.item_332()

    testeSorte = funções.Sorte()

    if testeSorte:
        input('Vá para 53')
        decisao_53()
    else:
        input('Vá para 160')
        decisao_272()


def decisao_180():
    H180 = historia.item_180()

    testeSorte = funções.Sorte()

    if testeSorte:
        input('Vá para 53')
        decisao_53()
    else:
        input('Vá para 160')
        decisao_272()


def decisao_53():
    H53 = historia.item_53()

    decisao = int(input('decisao :'))

    if decisao == 370:
        decisao_370()

    elif decisao == 348:
        decisao_348()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_370():
    H370 = historia.item_370()

    ComparaHabilidade = funções.ComparaHabilidade()
    # Se habilidade for menor que a soma dos dados, sege 104 se nao segue 342
    if ComparaHabilidade:
        input('Siga para 104:')
        decisao_104()
    else:
        input('Siga para 342')
        decisao_342()

def decisao_104():
    H104 = historia.item_104()

    input('Vá para 134')

    decisao_134()




def decisao_342():
    H342 = historia.item_342()

    decisao = int(input('decisao :'))

    if decisao == 294:
        decisao_294()

    elif decisao == 334:
        decisao_334()

    else:
        print(opção_incorreta)
        arte.GameOver()

  

def decisao_294():
    H294 = historia.item_294()

    funções.PerdeHabilidade(2)

    #informações do Monstro
    nomeMonstro = 'BESTA SANGRENTA'
    habilidade = 12
    energia = 10

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate_294(nomeMonstro)

    if Combate:
        print('Você venceu uma rodada!!')

        input("Agora teste sua sorte!\n")
        sorte = funções.Sorte()

        if sorte:
            decisao_97()
        else:
            decisao_21()

    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()


def decisao_97():
    H97 = historia.item_97()

    input('Vá para 134')

    decisao_134()


def decisao_21():
    H21 = historia.item_21()

    #informações do Monstro
    nomeMonstro = 'BESTA SANGRENTA (continuação)'
    habilidade = 12
    energia = 10

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate_294(nomeMonstro)

    if Combate:
        print('Você venceu uma rodada!!')

        input("Agora teste sua sorte!\n")
        sorte = funções.Sorte()

        if sorte:
            decisao_97()
        else:
            decisao_116()

    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()

def decisao_116():
    H116 = historia.item_116()

    arte.GameOver()
   

def decisao_134():
    H134 = historia.item_134()

    decisao = int(input('decisao :'))

    if decisao == 222:
        decisao_222()

    elif decisao == 247:
        decisao_247()

    else:
        print(opção_incorreta)
        arte.GameOver()

 
   



def decisao_334():
    H334 = historia.item_334()
   
    arte.GameOver()


def decisao_348():
    H348 = historia.item_348()

    ComparaHabilidade = funções.ComparaHabilidade()

    if ComparaHabilidade:
        input('Siga para 225:')
        decisao_225()
    else:
        input('Siga para 159')
        decisao_159()

def decisao_225():
    H225 = historia.item_225()

    #informações do Monstro
    nomeMonstro = 'BESTA SANGRENTA'
    habilidade = 12
    energia = 10

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate_294(nomeMonstro)

    if Combate:
        print('Você venceu uma rodada!!')

        input("Agora teste sua sorte!\n")
        sorte = funções.Sorte()

        if sorte:
            decisao_97()
        else:
            decisao_21()

    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()


def decisao_159():
    H159 = historia.item_159()

    if escolha_94_feita:
        input("Vá para 294")
        decisao_294()
    
    else:
        input("Vá para 294")
        decisao_334()

def decisao_272():
    H53 = historia.item_272()

    arte.GameOver()
    

   
def decisao_278():
    H278 = historia.item_278()

    input('Volte para 134')

    decisao_134()

   

def decisao_339():
    H339 = historia.item_339()

    funções.PerdeEnergia(1)

    decisao = int(input('decisao :'))

    if decisao == 303:
        decisao_303()

    elif decisao == 236:
        decisao_236()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_236():
    H236 = historia.item_236()

    #informações do Monstro
    nomeMonstro = 'IMITADOR'
    habilidade = 9
    energia = 8

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!!')
        decisao_314()
    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()


def decisao_314():

    H314 = historia.item_314()

    input('Volte para 262')

    decisao_262()



def decisao_303():
    H303 = historia.item_303()

    energia = habilidade = "DESCONHECIDA"

    funções.criarCriatura(energia,habilidade,'IMITADOR')

    input("Vá para 262")
    decisao_262()



def decisao_157():
    H157 = historia.item_157()

    funções.GanhaStatus(1,'sorte','🍀')

    input("Vá para 310")
    decisao_310()



def decisao_59():
    H59 = historia.item_59()

    decisao = int(input('decisao :'))

    if decisao == 341:
        decisao_341()

    elif decisao == 283:
        decisao_283()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_341():
    H341 = historia.item_344()

    decisao = int(input('decisao :'))

    if decisao == 367:
        decisao_367()

    elif decisao == 38:
        decisao_38()
    
    elif decisao == 169:
        decisao_169()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_38():
    H38 = historia.item_38()

    funções.PerdeEnergia(3)

    input('Vá para 109')

    decisao_109()

def decisao_169():
    H283 = historia.item_169()

    input('Vá para 109')

    decisao_109()



def decisao_367():
    H367 = historia.item_367()

    global escolha_367_feita

    escolha_367_feita = True

    decisao = int(input('decisao :'))

    if decisao == 244:
        decisao_244()

    elif decisao == 109:
        decisao_109()
    
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_244():
    H283 = historia.item_244()

    input('Vá para 109')

    decisao_109()

def decisao_283():
    H283 = historia.item_283()

    input('Volte para 109')

    decisao_109()


def decisao_109():
    H109 = historia.item_109()

    decisao = int(input('decisao :'))

    if decisao == 43:
        decisao_43()

    elif decisao == 24:
        decisao_24()


    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_43():
    H43 = historia.item_43()

    decisao = int(input('decisao :'))

    if decisao == 200:
        decisao_200()

    elif decisao == 316:
        decisao_316()


    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_200():
    H200 = historia.item_200()

    decisao = int(input('decisao :'))

    if decisao == 321:
        decisao_321()

    elif decisao == 316:
        decisao_316()


    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_321():
    H321 = historia.item_321()

    decisao = int(input('decisao :'))

    if decisao == 289:
        decisao_289()

    elif decisao == 316:
        decisao_316()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_289():
    H289 = historia.item_289()

    energia = habilidade = 'DESCONHECIDA'
    funções.criarCriatura(energia,habilidade,'MEDUSA')

    TesteSorte = funções.Sorte()

    if TesteSorte:
        input('Volte para 216')
        decisao_216()
    else:
        input('Volte para 19')
        decisao_19()


def decisao_19():
    H19 = historia.item_19()

    arte.GameOver()


def decisao_216():
    H216 = historia.item_216()

    decisao = int(input('decisao :'))

    if decisao == 308:
        decisao_308()

    elif decisao == 316:
        decisao_316()
    
    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_308():
    H216 = historia.item_308()

    input("Vá para 316")

    decisao_316()



def decisao_316():
    H316 = historia.item_316()

    decisao = int(input('decisao :'))

    if decisao == 296:
        decisao_296()

    elif decisao == 316:
        decisao_241()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_241():
    H216 = historia.item_241()

    decisao = int(input('decisao :'))

    if decisao == 393:
        decisao_393()

    elif decisao == 291:
        decisao_291()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_393():
    H393 = historia.item_393()

    decisao = int(input('decisao :'))

    if decisao == 274:
        decisao_274()

    elif decisao == 291:
        decisao_291()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_274():
    H274 = historia.item_274()

    ComparaHab = funções.ComparaHabilidade()

    if ComparaHab:
        input("Vá para 238")

        decisao_238()

    else:
        input("Vá para 359")

        decisao_359()

def decisao_359():
    H359 = historia.item_359()

    arte.GameOver()


def decisao_238():
    H238 = historia.item_238()

    funções.GanhaStatus(1,'habilidade','👊')

    input("Vá para 291")

    decisao_291()

def decisao_291():
    H291 = historia.item_291()

    input("Vá para 90")

    decisao_90()

def decisao_296():
    H216 = historia.item_296()

    decisao = int(input('decisao :'))

    if decisao == 49:
        decisao_49()

    elif decisao == 241:
        decisao_241()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_49():
    H49 = historia.item_49()

    decisao = int(input('decisao :'))

    if decisao == 205:
        decisao_205()

    elif decisao == 241:
        decisao_241()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_205():
    H205 = historia.item_205()

    decisao = int(input('decisao :'))

    if decisao == 306:
        decisao_306()

    elif decisao == 161:
        decisao_161()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_306():
    H306 = historia.item_306()

    funções.PerdeSorte(2)

    input("Vá para 29")

    decisao_29()


def decisao_161():
    H161 = historia.item_161()

    input("Vá para 29")

    decisao_29()


def decisao_29():
    H29 = historia.item_29()

    input("Vá para 90")

    decisao_90()


def decisao_24():
    H24 = historia.item_24()

    decisao = int(input('decisao :'))

    if decisao == 324:
        input("Vá para 324")
        decisao_324()

    elif decisao == 188:
        input("Vá para 188")
        decisao_188()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_324():
    H324 = historia.item_324()

    if escolha_367_feita:
        input("Vá para 256")

        decisao_256()
    
    else:
        input("Vá para 79")

        decisao_79()

def decisao_79():
    H79 = historia.item_79()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 106")

        decisao_106()
    
    else:
        input("Vá para 383")

        decisao_383()

def decisao_383():
    H383 = historia.item_383()

    input("Vá para 188")

    decisao_188()

def decisao_106():
    H106 = historia.item_106()

    input("Vá para 188")

    decisao_188()

def decisao_256():
    H256 = historia.item_256()

    input("Vá para 188")

    decisao_188()


def decisao_78():
    H78 = historia.item_78()

    decisao = int(input('decisao :'))

    if decisao == 301:
        decisao_301()

    elif decisao == 142:
        decisao_142()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_301():
    H301 = historia.item_301()

    decisao = int(input('decisao :'))

    if decisao == 162:
        decisao_162()

    elif decisao == 4:
        decisao_4()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_4():
    H4 = historia.item_4()

    arte.GameOver()

def decisao_162():
    H162 = historia.item_162()

    global escolha_162_feita
    escolha_162_feita = True

    funções.GanhaStatus(1,'sorte','🍀')

    input("Vá para 142")

    decisao_142()

def decisao_142():
    H142 = historia.item_142()

    input("Vá para 338")

    decisao_338()

def decisao_188():
    H188 = historia.item_188()

    decisao = int(input('decisao :'))

    if decisao == 155:
        decisao_155()

    elif decisao == 224:
        decisao_224()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_224():
    H224 = historia.item_224()

    input("Vá para 43")

    decisao_43()

def decisao_155():
    H155 = historia.item_155()

    decisao = int(input('decisao :'))

    if decisao == 378:
        decisao_378()

    elif decisao == 322:
        decisao_322()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_322():
    H322 = historia.item_322()

    input("Vá para 43")

    decisao_43()


def decisao_378():
    H378 = historia.item_378()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 112")
        decisao_112()
    
    else:
        input("Vá para 209")
        decisao_209()


def decisao_112():
    H112 = historia.item_112()

    input("Vá para 356")

    decisao_356()


def decisao_209():
    H209 = historia.item_209()

    input("Vá para 356")

    decisao_356()


def decisao_356():
    H356 = historia.item_356()

    input("Vá para 192")

    decisao_192()


def decisao_192():
    H192 = historia.item_192()

    decisao = int(input('decisao :'))

    if decisao == 120:
        decisao_120()

    elif decisao == 292:
        decisao_292()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_120():
    H120 = historia.item_120()

    decisao = int(input('decisao :'))

    if decisao == 228:
        decisao_228()

    elif decisao == 292:
        decisao_292()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_292():
    H292 = historia.item_292()

    decisao = int(input('decisao :'))

    if decisao == 93:
        decisao_93()

    elif decisao == 230:
        decisao_230()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_93():
    H93 = historia.item_93()

    decisao = int(input('decisao :'))

    if decisao == 284:
        decisao_284()

    elif decisao == 230:
        decisao_230()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_284():
    H284 = historia.item_284()

    if escolha_345_feita:
        decisao_398()

    else:
        decisao_57()

def decisao_398():
    H398 = historia.item_398()

    input("Vá para 230")

    decisao_230()

def decisao_57():
    H57 = historia.item_57()

    funções.PerdeEnergia(4)

    input("Vá para 198")

    decisao_198()

def decisao_198():
    H198 = historia.item_198()

    input("Vá para 230")

    decisao_230()

def decisao_230():
    H230 = historia.item_230()

    decisao = int(input('decisao :'))

    if decisao == 88:
        decisao_88()

    elif decisao == 5:
        decisao_5()
    
    elif decisao == 385:
        decisao_385()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_385():
    H385 = historia.item_385()

    decisao = int(input('decisao :'))

    if decisao == 318:
        decisao_318()

    elif decisao == 47:
        decisao_47()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_318():
    H318 = historia.item_318()

    if escolha_257_feita:
        decisao_86()
    
    else:
        decisao_276()

def decisao_86():
    H86 = historia.item_86()

    input("Vá para 187")

    decisao_187()

def decisao_47():
    H47 = historia.item_47()

    if escolha_257_feita:
        input("Vá para 10")
        decisao_10()
    
    else:
        input("Vá para 335")
        decisao_335()

def decisao_335():
    H335 = historia.item_335()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 67")
        decisao_67()
    
    else:
        input("Vá para 101")
        decisao_101()


def decisao_67():
    H67 = historia.item_67()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 146")
        decisao_146()
    
    else:
        input("Vá para 219")
        decisao_219()

def decisao_219():
    H219 = historia.item_219()

    arte.GameOver()

def decisao_146():
    H146 = historia.item_146()

    if escolha_257_feita:
        decisao_86()
    
    else:
        decisao_276()

def decisao_101():
    H101 = historia.item_101()

    arte.GameOver()


def decisao_187():
    H187 = historia.item_187()

    decisao = int(input('decisao :'))

    if decisao == 360:
        decisao_360()

    elif decisao == 280:
        decisao_280()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_360():
    H360 = historia.item_360()

    decisao = int(input('decisao :'))

    if decisao == 328:
        decisao_328()

    elif decisao == 297:
        decisao_297()
    
    elif decisao == 211:
        decisao_211()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_211():
    H211 = historia.item_211()

    #informações do Monstro
    nomeMonstro = 'ERVA'
    habilidade = 9
    energia = 9

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!!')
        decisao_201()
    else:
        print('Perdeu o combate, Você MORREU!')
        arte.GameOver()

def decisao_201():
    H201 = historia.item_201()

    global escolha_201_feita
    escolha_201_feita = True

    input("Vá para 305")
    
    decisao_305()


def decisao_297():
    H297 = historia.item_297()

    funções.PerdeSorte(1)

    input("Vá para 305")

    decisao_305()

def decisao_305():
    H305 = historia.item_305()

    if escolha_201_feita:
        decisao_253()

    else:
        decisao_148()

def decisao_253():
    H253 = historia.item_253()

    input("Vá para 315")

    decisao_315()

def decisao_148():
    H148 = historia.item_148()

    #info do monstro 1
    nomeMonstro = 'CÃO DE GUARDA'
    habilidade = 7
    energia = 7

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu o primeiro CÃO DE GUARDA!!')

        fuga = funções.Fuga()

        if fuga:
            input("Vá para 315")
            decisao_315()
        
        else:        
            print('Agora enfrentará o segundo CÃO DE GUARDA!')

            #info do monstro 2
            nomeMonstro1 = 'CÃO DE GUARDA'
            habilidade1 = 7
            energia1 = 8

            CriaCriatura = funções.criarCriatura(habilidade1,energia1,nomeMonstro1)
            Combate1 = funções.Combate(nomeMonstro1)

            if Combate1:
                print('Você venceu os dois CÃO DE GUARDA! Vá para 175')
                decisao_175()

            else:
                print(' Você perdeu o segundo combate! Você morreu!')
                arte.GameOver()
    else:
        print('Você perdeu o primeiro combate! Você Morreu!')
        arte.GameOver()

def decisao_175():
    H175 = historia.item_175()

    funções.GanhaStatus(2,'sorte','🍀')

    input("Vá para 315")
    decisao_315()

def decisao_315():
    H315 = historia.item_315()

    if escolha_171_feita:
        input("Vá para 129")
        decisao_129()
    
    else:
        input("Vá para 245")
        decisao_245()

def decisao_129():
    H129 = historia.item_129()

    decisao = int(input('decisao :'))

    if decisao == 349:
        decisao_349()

    elif decisao == 361:
        decisao_361()

    elif decisao == 167:
        decisao_167()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_349():
    H349 = historia.item_349()

    #info do monstro 1
    nomeMonstro = 'DIABO DO POÇO'
    habilidade = 12
    energia = 15

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu o DIABO DO POÇO!!')
        decisao_258()
    
    else:
        print('Você perdeu o combate! Você Morreu!')
        arte.GameOver()

def decisao_258():
    H258 = historia.item_258()

    decisao = int(input('decisao :'))

    if decisao == 95:
        decisao_95()

    elif decisao == 248:
        decisao_248()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_95():
    H95 = historia.item_95()

    funções.GanhaStatus(1,'habilidade','👊')

    input("Vá para 248")
    decisao_248()

def decisao_248():
    H248 = historia.item_248()

    input("Vá para 214")
    decisao_214()

def decisao_361():
    H361 = historia.item_361()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 82")
        decisao_82()
    
    else:
        input("Vá para 377")
        decisao_377()

def decisao_82():
    H82 = historia.item_82()

    input("Vá para 214")
    decisao_214()

def decisao_214():
    H214 = historia.item_214()

    decisao = int(input('decisao :'))

    if decisao == 389:
        decisao_389()

    elif decisao == 181:
        decisao_181()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_389():
    H389 = historia.item_389()

    global escolha_389_feita
    escolha_389_feita = True

    funções.PerdeHabilidade(4)

    input("Vá para 181")
    decisao_181()

def decisao_181():
    H181 = historia.item_181()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 312")
        decisao_312()
    
    else:
        input("Vá para 45")
        decisao_45()

def decisao_45():
    H45 = historia.item_45()

    funções.PerdeEnergia(4)
    funções.PerdeHabilidade(1)

    input("Vá para 312")
    decisao_312()

def decisao_312():
    H312 = historia.item_312()

    #info do monstro
    nomeMonstro = 'NINJA'
    habilidade = 11
    energia = 9

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu o NINJA!!')
        decisao_232()
    
    else:
        print('Você perdeu o combate! Você Morreu!')
        arte.GameOver()

def decisao_232():
    H232 = historia.item_232()

    if escolha_389_feita:
        input("Vá para 286")
        decisao_286()
    
    else:
        input("Vá para 320")
        decisao_320()

def decisao_286():
    H286 = historia.item_286()

    funções.GanhaStatus(4,'habilidade','👊')

    input("Vá para 320")
    decisao_320()

def decisao_320():
    H320 = historia.item_320()


    decisao = int(input('decisao :'))

    if decisao == 330:
        decisao_330()

    elif decisao == 269:
        decisao_269()

    elif decisao == 127:
        decisao_127()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_269():
    H269 = historia.item_269()
    global escolha_269_feita
    escolha_269_feita = True

    funções.GanhaStatus(3,'energia','⚡')

    if escolha_330_feita:
        input("Vá para 127")
        decisao_127()

    else:
        decisao = int(input('decisao :'))

        if decisao == 330:
            decisao_330()

        elif decisao == 127:
            decisao_127()

def decisao_127():
    H127 = historia.item_127()

    input("Vá para 90")
    decisao_90()

def decisao_330():
    H330 = historia.item_330()

    global escolha_330_feita
    escolha_330_feita = True

    funções.GanhaStatus(1,'energia','⚡')

    if escolha_269_feita:
        input("Vá para 127")
        decisao_127()
    else:
        decisao = int(input('decisao :'))

        if decisao == 269:
            decisao_269()

        elif decisao == 127:
            decisao_127()

def decisao_167():
    H167 = historia.item_167()

    funções.PerdeEnergia(4)

    input('Siga para 203')

    decisao_203()

def decisao_377():
    H377 = historia.item_377()

    funções.PerdeEnergia(5)

    input("Vá para 203")
    decisao_203()

def decisao_203():
    H203 = historia.item_203()

    #info do monstro 1
    nomeMonstro = 'DIABO DO POÇO'
    habilidade = 12
    energia = 15

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu o DIABO DO POÇO!!')
        decisao_258()
    
    else:
        print('Você perdeu o combate! Você Morreu!')
        arte.GameOver()

def decisao_245():
    H245 = historia.item_245()

    #info do monstro
    nomeMonstro = 'DIABO DO POÇO'
    habilidade = 12
    energia = 15

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu o DIABO DO POÇO!!')
        decisao_258()
    
    else:
        print('Você perdeu o combate! Você Morreu!')
        arte.GameOver()


def decisao_328():
    H328 = historia.item_328()

    decisao = int(input('decisao :'))

    if decisao == 125:
        decisao_125()

    elif decisao == 99:
        decisao_99()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_99():
    H99 = historia.item_99()

    decisao = int(input('decisao :'))

    if decisao == 266:
        decisao_266()

    elif decisao == 305:
        decisao_305()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_266():
    H266 = historia.item_266()

    input("Vá para 305")

    decisao_305()

def decisao_125():
    H125 = historia.item_125()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 69")
        decisao_69()
    
    else:
        input("Vá para 139")
        decisao_139()
    
def decisao_69():
    H69 = historia.item_69()

    input("Vá para 305")
    decisao_305()

def decisao_139():
    H139 = historia.item_139()

    #info do monstro
    nomeMonstro = 'ERVA'
    habilidade = 9
    energia = 9

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu a ERVA!!')
        decisao_201()
    
    else:
        print('Você perdeu o combate! Você Morreu!')
        arte.GameOver()

def decisao_280():
    H280 = historia.item_280()

    input("Vá para 218")

    decisao_218()

def decisao_276():
    H276 = historia.item_276()

    arte.GameOver()

def decisao_10():
    H10 = historia.item_10()

    if escolha_257_feita:
        decisao_86()
    
    else:
        decisao_276()

def decisao_5():
    H5 = historia.item_5()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 185")
        decisao_185()
    
    else:
        input("Vá para 395")
        decisao_395()

def decisao_395():
    H395 = historia.item_395()

    funções.PerdeEnergia(3)
    
    input("Vá para 259")
    decisao_259()

def decisao_259():
    H259 = historia.item_259()

    decisao = int(input('decisao :'))

    if decisao == 318:
        decisao_318()

    elif decisao == 47:
        decisao_47()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_185():
    H185 = historia.item_185()

    decisao = int(input('decisao :'))

    if decisao == 318:
        decisao_318()

    elif decisao == 47:
        decisao_47()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_88():
    H88 = historia.item_88()

    decisao = int(input('decisao :'))

    if decisao == 343:
        decisao_343()

    elif decisao == 268:
        decisao_268()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_268():
    H268 = historia.item_268()

    arte.GameOver()

def decisao_343():
    H343 = historia.item_343()

    funções.PerdeEnergia(1)

    decisao = int(input('decisao :'))

    if decisao == 318:
        decisao_318()

    elif decisao == 47:
        decisao_47()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_228():
    H228 = historia.item_228()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 150")
        decisao_150()
    
    else:
        input("Vá para 33")
        decisao_33()

def decisao_150():
    H150 = historia.item_150()

    funções.PerdeHabilidade(1)

    input("Vá para 292")
    decisao_292()

def decisao_33():
    H33 = historia.item_33()

    funções.PerdeHabilidade(3)

    input("Vá para 292")
    decisao_292()

def decisao_394():
    H394 = historia.item_394()

    jogada = jogaDADOS.jogaDados(dado)
    print(f"🎲:{jogada}")
    jogada += 2
    print(f"Total: {jogada}")
    funções.PerdeEnergia(jogada)

    decisao = int(input('decisao :'))

    if decisao == 14:
        decisao_14()

    elif decisao == 59:
        decisao_59()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_108():
    H108 = historia.item_108()

    decisao = int(input('decisao :'))

    if decisao == 394:
        decisao_394()

    elif decisao == 59:
        decisao_59()

    elif decisao == 14:
        decisao_14()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_121():
    H121 = historia.item_121()

    decisao = int(input('decisao :'))

    if decisao == 26:
        decisao_26()

    elif decisao == 354:
        decisao_354()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_26():
    H26 = historia.item_26()

    funções.PerdeHabilidade(2)

    comparaHab = funções.ComparaHabilidade()

    if comparaHab:
        input("Vá para 55")
        decisao_55()
    
    else:
        input("Vá para 202")
        decisao_202()

def decisao_354():
    H354 = historia.item_354()

    funções.PerdeSorte(2)

    comparaHab = funções.ComparaHabilidade()

    if comparaHab:
        input("Vá para 55")
        decisao_55()
    
    else:
        input("Vá para 202")
        decisao_202()

def decisao_365():
    H365 = historia.item_365()

    decisao = int(input('decisao :'))

    if decisao == 290:
        decisao_290()

    elif decisao == 191:
        decisao_191()

    elif decisao == 84:
        decisao_84()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_64():
    H64 = historia.item_64()

    ComparaHab = funções.ComparaHabilidade()

    if ComparaHab:
        input("Vá para 115")
        decisao_115()
    else:
        input("Vá para 190")
        decisao_190()

def decisao_115():
    H115 = historia.item_115()

    funções.GanhaStatus(3,'energia','⚡')
    
    input("Vá para 221")
    decisao_221()

def decisao_190():
    H190 = historia.item_190()

    funções.PerdeEnergia(3)
    
    input("Vá para 50")
    decisao_50()

def decisao_50():
    H50 = historia.item_50()

    input("Vá para 221")
    decisao_221()

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
    H154 = historia.item_154()

    input('Volte para 22')

    decisao_22()


def decisao_137():
    H137 = historia.item_137()
    decisao = int(input('decisao :'))

    if decisao == 220:
        decisao_220()

    elif decisao == 362:
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
    funções.Provisoes()
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

    funções.PerdeEnergia(6)

    decisao_20()
   

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
            decisao_9()

        else:
            print(' Você perdeu o segundo combate! Você morreu!')
            arte.GameOver()
    else:
        print('Você perdeu o primeiro combate! Você Morreu!')
        arte.GameOver()

def decisao_9():
    H9 = historia.item_9()
    decisao = int(input('decisao :'))
    

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
    
    ComparaHabilidade = funções.ComparaHabilidade()

    if ComparaHabilidade:
        print("Vá para 80")
        decisao_80()
    
    else:
        print("Vá para 246")
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
        input('Siga para 313')
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

    input('Vá para 275')
    decisao_275()
   

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

    H239 = historia.item_239()

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

    global escolha_251_feita
    escolha_251_feita = True

    input('Aperte ENTER para seguir para 344')

    decisao_344()



def decisao_133():
    H133 = historia.item_133()

    ComparaHabilidade = funções.ComparaHabilidade()

    if ComparaHabilidade:
        input("Vá para 178")
        decisao_178()
    
    else:
        input("Vá para 17")
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

def decisao_271():
    H271 = historia.item_271()

    funções.PerdeHabilidade(1)

    input("Vá para 237")
    decisao_237()

def decisao_237():
    H237 = historia.item_237()

    decisao = int(input('decisão : '))

    if decisao == 12:
        decisao_12()
    
    elif decisao == 100:
        decisao_100()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_12():
    H12 = historia.item_12()

    decisao = int(input('decisão : '))

    if decisao == 382:
        decisao_382()
    
    elif decisao == 195:
        decisao_195()
    
    elif decisao == 250:
        decisao_250()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_382():
    H382 = historia.item_382()

    decisao = int(input('decisão : '))

    if decisao == 144:
        decisao_144()
    
    elif decisao == 227:
        decisao_227()
    
    elif decisao == 391:
        decisao_391()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_144():
    H144 = historia.item_144()

    input('volte para 85')

    decisao_85()

def decisao_227():
    H227 = historia.item_227()

    input('volte para 85')

    decisao_85()

def decisao_391():
    H391 = historia.item_391()

    funções.GanhaStatus(1,'energia','⚡')
    funções.GanhaStatus(1,'habilidade','👊')
    funções.GanhaStatus(1,'sorte','🍀')

    input('Volte para 100')

    decisao_100()

    
     
def decisao_85():
    H85 = historia.item_85()

    arte.GameOver()

    

def decisao_195():
    H195 = historia.item_195()

    funções.PerdeEnergia(1)

    input('Vá para 382')

    decisao_382()


def decisao_250():
    H250 = historia.item_250()

    decisao = int(input('decisão : '))

    if decisao == 44:
        decisao_44()
    
    elif decisao == 195:
        decisao_195()
    
    elif decisao == 382:
        decisao_382()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_44():
    H44 = historia.item_44()

    arte.GameOver()


def decisao_100():
    H100 = historia.item_100()

    decisao = int(input('decisão : '))

    if decisao == 87:
        decisao_87()
    
    elif decisao == 217:
        decisao_217()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_87():
    H87 = historia.item_87()

    input('Va para 381')

    decisao_381()

def decisao_217():
    H217 = historia.item_217()

    funções.PerdeHabilidade(1)

    input('Va para 36')

    decisao_36()

def decisao_36():
    H36 = historia.item_36()

    comparaHabeEnergia = funções.ComparaHabilidadeEEnergia()

    if comparaHabeEnergia:
        input("Vá´para 340")
        decisao_340()

    else:
        input("Vá para 7")
        decisao_7()

def decisao_340():
    H340 = historia.item_340()

    input('Va para 381')

    decisao_381()

def decisao_381():
    H381 = historia.item_381()

    decisao = int(input('decisão : '))

    if decisao == 331:
        decisao_331()
    
    elif decisao == 128:
        decisao_128()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_128():
    H128 = historia.item_128()

    decisao = int(input('decisão : '))

    if decisao == 35:
        decisao_35()
    
    elif decisao == 233:
        decisao_233()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_233():
    H233 = historia.item_233()

    arte.GameOver()

def decisao_35():
    H35 = historia.item_35()

    decisao = int(input('decisão : '))

    if decisao == 333:
        decisao_333()
    
    elif decisao == 124:
        decisao_124()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_333():
    H333 = historia.item_333()

    arte.GameOver()

def decisao_DUVIDA124():
    H124 = historia.item_124()
################dÚVIDA####################3333333333333333333333333333333
    arte.GameOver()


def decisao_81():
    H81 = historia.item_81()

    decisao = int(input('decisão : '))

    if decisao == 307:
        decisao_307()
    
    elif decisao == 263:
        decisao_263()
    
    elif decisao == 136:
        decisao_136()
    
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_263():
    H263 = historia.item_263()

    decisao = int(input('decisão : '))

    if decisao == 153:
        decisao_153()
    
    elif decisao == 74:
        decisao_74()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_153():
    H153 = historia.item_153()

    decisao = int(input('decisão : '))

    if decisao == 390:
        decisao_390()
    
    elif decisao == 371:
        decisao_371()
    
    elif decisao == 74:
        decisao_74()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_371():
    H371 = historia.item_371()

    comparaHab = funções.ComparaHabilidade

    if comparaHab:
        input("Vá para 273")
        decisao_273()

    else:
        input("Vá para 113")
        decisao_113()

def decisao_113():
    H113 = historia.item_113()

    decisao = int(input('decisão : '))

    if decisao == 371:
        decisao_371()
    
    elif decisao == 74:
        decisao_74()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_273():
    H273 = historia.item_273()
    
    decisao = int(input('decisão : '))

    if decisao == 15:
        decisao_15()
    
    elif decisao == 204:
        decisao_204()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_204():
    H204 = historia.item_204()

    sorte = funções.Sorte()

    if sorte:
        input("Vá para 131")
        decisao_131()
    
    else:
        input("Vá para 199")
        decisao_199()

def decisao_131():
    H131 = historia.item_131()

    input("Vá para 74")

    decisao_74()

def decisao_15():
    H15 = historia.item_15()

    input("Vá para 74")

    decisao_74()

def decisao_199():
    H199 = historia.item_199()

    funções.PerdeEnergia(2)
    funções.PerdeSorte(1)

    input("Vá para 74")

    decisao_74()

def decisao_390():
    H390 = historia.item_390()
    
    funções.GanhaStatus(1,'sorte','🍀')

    decisao = int(input('decisão : '))

    if decisao == 15:
        decisao_15()
    
    elif decisao == 204:
        decisao_204()

    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_74():
    H74 = historia.item_74()

    if escolha_251_feita: 
        print("\n--- você possui o anel dos desejos, pode seguir para 265, se quiser ---\n")
        decisao = int(input('decisão : '))

        if decisao == 265:
            decisao_265()
        
        elif decisao == 300:
            decisao_300()
        
        elif decisao == 327:
            decisao_327()

        else:
            print(opção_incorreta)
            arte.GameOver()
    else:
        print("\n--- você não possui o anel dos desejos, o caminho 265 está bloqueado ---\n")
        decisao = int(input('decisão : '))
        
        if decisao == 300:
            decisao_300()
        
        elif decisao == 327:
            decisao_327()

        else:
            print(opção_incorreta)
            arte.GameOver()

def decisao_265():
    H265 = historia.item_265()

    input("Vá para 122")
    decisao_122()


def decisao_300():
    H300 = historia.item_300()

    decisao = int(input('decisão : '))

    if decisao == 141:
        decisao_141()
    
    elif decisao == 327:
        decisao_327()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_327():
    H327 = historia.item_327()

    #info do monstro 
    nomeMonstro = 'DEMÔNIO DO ESPELHO'
    habilidade = 8
    energia = 6

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate_327(nomeMonstro)

    if Combate == 1:
        print('Você perdeu uma série, vá para 8!')
        decisao_8()

    elif Combate == 2:
        print('Você venceu o combate sem perder nenhuma série, vá para 92!')
        decisao_92()
    
    else:
        print("Você perdeu o combate!")
        arte.GameOver()

def decisao_8():
    H8 = historia.item_8()

    arte.GameOver()

def decisao_92():
    H92 = historia.item_92()

    input("Vá para 122")
    decisao_122()

def decisao_307():
    H307 = historia.item_307()

    decisao = int(input('decisão : '))

    if decisao == 263:
        decisao_263()
    
    elif decisao == 136:
        decisao_136()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_136():
    H136 = historia.item_136()

    decisao = int(input('decisão : '))

    if decisao == 210:
        decisao_210()
    
    elif decisao == 78:
        decisao_78()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_210():
    H210 = historia.item_210()

    decisao = int(input('decisão : '))

    if decisao == 27:
        decisao_27()
    
    elif decisao == 78:
        decisao_78()

    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_27():
    H27 = historia.item_27()

    input("Vá para 78")
    decisao_78()

def decisao_331():
    H331 = historia.item_331()

    #info do monstro 
    nomeMonstro = 'GUERREIRO-ESQUELETO'
    habilidade = 8
    energia = 6

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu!')
        decisao_71()
    else:
          print('Você perdeu o Combate!')
          arte.GameOver()

def decisao_71():
    H71 = historia.item_71()

    input('Va para 128')

    decisao_128()

def decisao_7():
    H7 = historia.item_7()

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

def decisao_160():
    H160 = historia.item_160()

    input('Va para 237')

    decisao_237()


def decisao_319():
    H319 = historia.item_319()

    input('Va para 285')

    decisao_285()

def decisao_212():
    H212 = historia.item_212()

    input('Va para 285')

    decisao_285()



def decisao_285():
    H285 = historia.item_285()

    funções.PerdeEnergia(2)
    funções.PerdeHabilidade(1)

    input('Va para 237')

    decisao_237()


def decisao_254():
    H254 = historia.item_254()

    #informações do Monstro
    nomeMonstro = 'VERME DA ROCHA'
    habilidade = 7
    energia = 11

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate_254(nomeMonstro)

    ### Pode fugir para 117 após duas séries de ataque

    if Combate == 2:
        print('Você venceu!!')
        decisao_76()
    elif Combate == 1:
        input("Você fugiu, vá para 117")
        decisao_117()
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

def decisao_329():
    H329 = historia.item_329()

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

    global escolha_94_feita
    escolha_94_feita = True

    input('Aperte ENTER para seguir para 174')

    decisao_174()


def decisao_174():
    H174 = historia.item_174()

    Sorte = funções.Sorte()

    if Sorte:
        input('Vá para 39')
        decisao_39()
    
    else:
        input('Vá para 350')
        decisao_350()



def decisao_350():
    H350 = historia.item_350()

    PerdeEnergia = funções.PerdeEnergiaNoDado()

    if PerdeEnergia:
        input('va para 39')
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
    
    Fuga = funções.Fuga()

    if Fuga:
        input('Aperte ENTER para seguir para 267')
        decisao_267()
    
    else:
        Combate = funções.Combate(nomeMonstro)
        if Combate:
            print('Você venceu!!')
            input('Siga para 111')
            decisao_111()
        else:
            print('Perdeu o combate, Você MORREU!')
            arte.GameOver()


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
    elif decisao == 34:
        decisao_34()
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

    funções.PerdeEnergia(2)
   
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
            input('Vá para 364')
            decisao_364()
        
        else:
            print('Você perdeu o combate! Você Morreu!')
            arte.GameOver()
    else:
        print('Acabou sua energia! Você Morreu!')
        arte.GameOver()


def decisao_364():

    H364 = historia.item_364()

    decisao = int(input('decisão : '))

    if decisao == 31:
        decisao_31()
    elif decisao == 3:
        decisao_3()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_31():

    H31 = historia.item_31()

    decisao = int(input('decisão : '))

    if decisao == 376:
        decisao_376()
    elif decisao == 3:
        decisao_3()
    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_376():

    H376 = historia.item_376()

    decisao = int(input('decisão : '))

    if decisao == 62:
        decisao_62()
    elif decisao == 3:
        decisao_3()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_62():

    H62 = historia.item_62()

    decisao = int(input('decisão : '))

    if decisao == 16:
        decisao_16()
    elif decisao == 392:
        decisao_392()
    elif decisao == 177:
        decisao_177()
    
    elif decisao == 287:
        decisao_287()

    elif decisao == 132:
        decisao_132()

    elif decisao == 249:
        decisao_249()
    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_16():

    H16 = historia.item_16()

    funções.PerdeEnergiaNoDado(1,1)

    decisao = int(input('decisão : '))

    if decisao == 16:
        decisao_16()
    elif decisao == 392:
        decisao_392()
    elif decisao == 177:
        decisao_177()
    
    elif decisao == 287:
        decisao_287()

    elif decisao == 132:
        decisao_132()

    elif decisao == 249:
        decisao_249()
    else:
        print(opção_incorreta)
        arte.GameOver()

    

def decisao_392():

    H392 = historia.item_392()

    funções.PerdeEnergiaNoDado(1,1)

    decisao = int(input('decisão : '))

    if decisao == 16:
        decisao_16()
    elif decisao == 392:
        decisao_392()
    elif decisao == 177:
        decisao_177()
    
    elif decisao == 287:
        decisao_287()

    elif decisao == 132:
        decisao_132()

    elif decisao == 249:
        decisao_249()
    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_177():
    H177 = historia.item_177()

    TesteSorte = funções.Sorte()

    if TesteSorte:
        input('Va para 243')
        decisao_243()
    else:
        input('va para 103')
        decisao_103()

    
 
def decisao_243():
    H177 = historia.item_243()

    input('Vá para 400')

    decisao_400()


def decisao_103():
    H177 = historia.item_103()

    funções.PerdeEnergia(3)

    input('volte para 77')

    decisao_77()

    
def decisao_77():
    H177 = historia.item_77()

    input('Vá para 400')

    decisao_400() 


       
def decisao_400():
    H400 = historia.item_400()  

    arte.Winner()


def decisao_287():
    H287 = historia.item_287()

    funções.PerdeEnergiaNoDado(1,1)

    decisao = int(input('decisão : '))

    if decisao == 16:
        decisao_16()
    elif decisao == 392:
        decisao_392()
    elif decisao == 177:
        decisao_177()
    
    elif decisao == 287:
        decisao_287()

    elif decisao == 132:
        decisao_132()

    elif decisao == 249:
        decisao_249()
    else:
        print(opção_incorreta)
        arte.GameOver()


    
   
def decisao_132():
    H132 = historia.item_132()

    funções.PerdeEnergiaNoDado(1,1)

    decisao = int(input('decisão : '))

    if decisao == 16:
        decisao_16()
    elif decisao == 392:
        decisao_392()
    elif decisao == 177:
        decisao_177()
    
    elif decisao == 287:
        decisao_287()

    elif decisao == 132:
        decisao_132()

    elif decisao == 249:
        decisao_249()
    else:
        print(opção_incorreta)
        arte.GameOver()



def decisao_249():
    H249 = historia.item_249()

    funções.PerdeEnergiaNoDado(1,1)

    decisao = int(input('decisão : '))

    if decisao == 16:
        decisao_16()
    elif decisao == 392:
        decisao_392()
    elif decisao == 177:
        decisao_177()
    
    elif decisao == 287:
        decisao_287()

    elif decisao == 132:
        decisao_132()

    elif decisao == 249:
        decisao_249()
    else:
        print(opção_incorreta)
        arte.GameOver()


def decisao_3():

    H3 = historia.item_3()

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

def decisao_166():
    H166 = historia.item_166()

    funções.PerdeHabilidade(3)

    #info do monstro 1
    nomeMonstro = 'GUARDIÃO VOADOR'
    habilidade = 7
    energia = 8

    CriaCriatura = funções.criarCriatura(habilidade,energia,nomeMonstro)
    Combate = funções.Combate(nomeMonstro)

    if Combate:
        print('Você venceu o primeiro GUARDIÃO VOADOR!!')
        print('Agora enfrenará o segundo GUARDIÃO VOADOR!')

        #info do monstro 2
        nomeMonstro1 = 'GUARDIÃO VOADOR'
        habilidade1 = 8
        energia1 = 8

        CriaCriatura = funções.criarCriatura(habilidade1,energia1,nomeMonstro1)
        Combate1 = funções.Combate(nomeMonstro1)

        if Combate1:
            print('Você venceu os dois GUARDIÃO VOADOR! Vá para 9')
            decisao_11()

        else:
            print(' Você perdeu o segundo combate! Você morreu!')
            arte.GameOver()
    else:
        print('Você perdeu o primeiro combate! Você Morreu!')
        arte.GameOver()

def decisao_11():
    H11 = historia.item_11()

    decisao = int(input('decisão : '))

    if decisao == 140:
        decisao_140()

    elif decisao == 46:
        decisao_46()
    else:
        print(opção_incorreta)
        arte.GameOver()

def decisao_46():
    H46 = historia.item_46()

    input('volte para 239')
    decisao_239()

def decisao_140():
    H140 = historia.item_140()

    arte.GameOver()

def decisao_358():
    H358 = historia.item_358()

    funções.PerdeEnergia(2)

    input('volte para 239')
    decisao_239()
   


def decisao_275():
    H275 = historia.item_275()

    #checagem de sorte

    if funções.Sorte():
        input('Vá para 231')
        decisao_231()
    else:
        input('Vá para 309')
        decisao_309()


def decisao_231():
    H231 = historia.item_231()

    input('Aperte ENTER para seguir para 110')

    decisao_110()


def decisao_309():
    H309 = historia.item_309()

    funções.PerdeEnergia(3)

    Sorte = funções.Sorte()
    print('----------------------------------------------')
    if Sorte:
        print('Você foi redirecionado para 231!')
        decisao_231()
    else:
        print('Você foi redirecionado para 193!')
        decisao_193()

      


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
        decisao_9()
    else:
          print('Você perdeu o Combate!')
          arte.GameOver()
