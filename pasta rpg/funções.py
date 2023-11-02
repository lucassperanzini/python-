import jogaDADOS
import arte

dado = 0

# Dicionários que mantêm o estado do personagem e das criaturas
StatusIniciais = {}
StatusAtuais = {}


def funcPocao():
       
    pocaoHabilidade = 'Pocao Habilidade'
    pocaoForça = 'Pocao Forca'
    pocaoFortuna = 'Pocao Sorte'

    Escolha_Pocao = int(input('''

           (1) Poção da Habilidade - repõe os pontos de HABILIDADE. Poção da Força - repõe os pontos de ENERGIA.
           (2) Poção da Força - repõe os pontos de ENERGIA
           (3)Poção da Fortuna - repõe os pontos de SORTE e acrescenta 1 ponto à SORTE Inicial.

            '''))
    if Escolha_Pocao == 1:
        return pocaoHabilidade
    elif Escolha_Pocao == 2:
        return pocaoForça
    elif Escolha_Pocao == 3:
        return pocaoFortuna
    



def CriarPersonagem():

    def funcHabilidade():
        habilidade = Jogada  + 6

        return habilidade
    
    def funcEnergia():
       energia = Jogada + Jogada2 + 12

       return energia
    
    def funcSorte():
        sorte = Jogada + 6

        return sorte
    

    
    Jogada = jogaDADOS.jogaDados(dado)
    Jogada2 = jogaDADOS.jogaDados(dado)

    TipoPoção = funcPocao()

    print(f" o opção ESCOLHIDA foi : {TipoPoção}")


    # dicionario que guarda Status do personagem
    global StatusIniciais

    StatusIniciais = {

        'FolhaDeAventura':{
            'habilidade': funcHabilidade(),
            'energia':funcEnergia(),
            'sorte':funcSorte(),
            'provisoes':10,
            TipoPoção:1
            
        }
        
    }
    global StatusAtuais

    StatusAtuais = {

        'FolhaDeAventura':{
            'habilidade': funcHabilidade(),
            'energia':funcEnergia(),
            'sorte':funcSorte(),
            'provisoes':10,
             TipoPoção:1
            
        }
        
    }



    # print das informações do dicionario
    print('\n-------------------INFORMAÇÕES INICIAIS--------------------------')
    print(F'\n   🎲 : {Jogada}\n\n   🎲 : {Jogada2}\n')
    print(f'''    Habilidade : {StatusIniciais['FolhaDeAventura']['habilidade']}
          
    Energia : {StatusIniciais['FolhaDeAventura']['energia']}

    Sorte: {StatusIniciais['FolhaDeAventura']['sorte']}

    Provisões: {StatusIniciais['FolhaDeAventura']['provisoes']} 

    Poção : {TipoPoção} : {StatusIniciais['FolhaDeAventura'][TipoPoção]}

    

--------------------------------------------------------------------------------
''')




# Função para criar uma criatura
def criarCriatura(habilidade, energia, nomeMonstro):
    global StatusAtuais

    if 'EncontrosMonstros' not in StatusAtuais:
        StatusAtuais['EncontrosMonstros'] = {}
    
    StatusAtuais['EncontrosMonstros'][nomeMonstro] = {
        'habilidade': habilidade,
        'energia': energia,
        'energiaAtual':energia
    }

    print(StatusAtuais)



# Função para medir força de ataque
def ForçaDeAtaque(nomeMonstro=None):
    Jogada = jogaDADOS.jogaDados(dado)
    Jogada2 = jogaDADOS.jogaDados(dado)

    print(f'\n🎲 : {Jogada}\n\n🎲 : {Jogada2}')

    global StatusAtuais
    
    if nomeMonstro:
        força = StatusAtuais['EncontrosMonstros'][nomeMonstro]['habilidade'] + (Jogada + Jogada2)
    else:
        força = StatusAtuais['FolhaDeAventura']['habilidade'] + (Jogada + Jogada2)

    return força


def Fuga():
    #pode escapar de um combate
    # perde -2 de energia por ser covarde
    #pode usar sorte no ferimento
    # so pode fugir de acordo com instruções específicas

    decisao = input("Deseja fugir do combate? ").lower()

    if decisao == 'sim':

        decisao1 = input("Deseja testar a sorte para tomar menos dano? ").lower()

        if decisao1 == 'sim':

            sorte = Sorte()

            if sorte:

                ## Se tiver sorte Perde Energia ??
                print("A sorte está ao seu lado!!\nSiga seu caminho sem perder Energia!!")

            else:
                print("hahaha parece que a sorte não está do seu lado\nPerdeu 2 de Energia!!")

                PerdeStatus(2,'energia',"⚡")

        
        else:
            print("Fugiu do combate, medroso!!\n Perdeu 2 de Energia!!")

            PerdeStatus(2,'energia',"⚡")

        
        return True

    else:
        return False
    


def Sorte():
    tiveSorte = False

    Jogada = jogaDADOS.jogaDados(dado)
    Jogada2 = jogaDADOS.jogaDados(dado)

 
    global StatusAtuais

    sorte = StatusAtuais['FolhaDeAventura']['sorte']

    if sorte <= 0:
        print('Acabou sua Sorte')
    else:

        print('Vamos ver se você tem sorte ou não!!')
        print(f'Sorte Atual: {sorte}')

        print(F'\n🎲 : {Jogada}\n\n🎲 : {Jogada2}')


        somaDados = Jogada + Jogada2

        if somaDados <= sorte:
            tiveSorte = True
            print('\nResultado favorável!Teve sorte')
        else:
            tiveSorte = False
            print('\nPerdeu haha nao foi dessa vez!')
            print('Você Sofrerá as consequências!')
           

        sorte -= 1

           
        print(f'\nComo usou o recurso Sorte perde 1 ponto | Sorte ATUAL: {sorte} ')

        StatusAtuais['FolhaDeAventura']['sorte'] = sorte

        #Retorna True ou False se ele teve sorte
        return tiveSorte
    



def Combate(nomeMonstro):

    # numero de rounds
    contadorBatalhas = 1

    #Valor do dano
    DanoCrítico = 4
    DanoCríticoP = 3
    DanoComum = 2
    DanoReduzido = 1

    global StatusAtuais
    
    # energia do personagem / criatura
    EnergiaPersonagem = StatusAtuais['FolhaDeAventura']['energia']
    EnergiaCriatura = StatusAtuais['EncontrosMonstros'][nomeMonstro]['energiaAtual']


    # enquanto ou a energia do personagem ou da criatura diferente de 0 continua a batalha
    while EnergiaPersonagem > 0 and EnergiaCriatura > 0: 

        input('\nVamos comçar o combate? Aperte ENTER para iniciar ')

        print('\n\n--------Início do Combate-----------')
        print(f'\nRound {contadorBatalhas}')
        print('\nPersonagem :')

        #Função que determina a força do personagem
        ForçaPersonagem = ForçaDeAtaque()

        print(f'\nForça do Personagem : 👊 {ForçaPersonagem}')
        print('------------------------------------------------')
            
        print(nomeMonstro)

        #Função que determina a força da criatura
        ForçaCriatura = ForçaDeAtaque(nomeMonstro)

        print(f'\nForça {nomeMonstro}: 👊 {ForçaCriatura}')
        print('------------------------------------------------')

        # Se a força for maior que da criatura : criatura perde pontos
        if ForçaPersonagem > ForçaCriatura:
            print('Você feriu a Criatura!😀\n')

            resposta = input('Você quer Testar sua sorte? (Sim/Não)').lower()

            if resposta == 'sim':

                testeSorte = Sorte()

                if testeSorte:
                    EnergiaCriatura -= DanoCrítico
                    print(f'Dano Crítico! -4 pontos de energia da {nomeMonstro}| Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')
                else:
                    EnergiaCriatura -= DanoReduzido
                    print(f'Dano reduzido! -1 ponto de energia | Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')

            else:
                 EnergiaCriatura -= DanoComum
                 print(f' {nomeMonstro} sofreu -2 pontos de energia | Energia atual⚡{EnergiaCriatura}')
                 print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')

            
        # se a força for menor que da criatura, personagem perde pontos
        elif ForçaPersonagem < ForçaCriatura:
            print('Você foi ferido pela Criatura!😨')

            resposta = input('Você quer Testar sua sorte para ter chance de reduzir o dano? (Sim/Não)').lower()


            if resposta == 'sim':
                testeSorte = Sorte()


                if testeSorte:
                    EnergiaPersonagem -= DanoReduzido
                    print(f'Minimizou o ferimento! -1 pontos de energia do personagem | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')
                else:
                    EnergiaPersonagem -= DanoCríticoP
                    print(f'Ferimento grave! -3 ponto de energia | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')

            else:
                EnergiaPersonagem -= DanoComum
                print(f' Você sofreu -2 pontos de energia | Energia atual⚡{EnergiaPersonagem}')
                print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')


           
            
        # se for igual, nao acontece nada
        elif ForçaPersonagem == ForçaCriatura:
            print('Golpé Neutralizado, forças iguais!')
            print('Que começe a próxima série de ataque!')

        print('-------------------------------------------')

        contadorBatalhas +=1

        StatusAtuais['FolhaDeAventura']['energia'] = EnergiaPersonagem

        



    if EnergiaPersonagem > EnergiaCriatura:
         return True
    else:
         return False


############# Funções específicas da história ###############################

def GanhaStatus(valor,elemento,emoji):

    #PROBLEMA NA FUNÇÃO STATUS    
    global StatusAtuais, StatusIniciais

    ValorElemento = StatusAtuais['FolhaDeAventura'][elemento]

    print(f'\n{elemento} anterior {emoji}',ValorElemento)

    
    Elementoinicial =  StatusIniciais['FolhaDeAventura'][elemento]
    

    if ValorElemento + valor > Elementoinicial:
        print(f'{elemento} ultrapassou valor Inicial.')
        ValorElemento = Elementoinicial

    else:
        print(f'{elemento} aumentou em {valor}.')
        ValorElemento += valor
    
    StatusAtuais['FolhaDeAventura'][elemento] = ValorElemento 
    
    print(f'{elemento} atual {emoji} ', ValorElemento)




def PerdeStatus(valor,elemento,emoji):

    #PROBLEMA NA FUNÇÃO STATUS    
    global StatusAtuais, StatusIniciais

    ValorElemento = StatusAtuais['FolhaDeAventura'][elemento]

    print(f'\n{elemento} anterior {emoji}',ValorElemento)
    

    if elemento == "energia" and ValorElemento - valor <= 0:
        print("\n---Sua energia acabou!!--- \nSua aventura termina aqui!")
        arte.GameOver()
        exit()

    else:
        print(f'{elemento} diminuiu em {valor}.')
        ValorElemento -= valor
    
    StatusAtuais['FolhaDeAventura'][elemento] = ValorElemento 
    
    print(f'{elemento} atual {emoji} ', ValorElemento)



def farpasMenosEnergia():

    global StatusAtuais
           
    energia = StatusAtuais['FolhaDeAventura']['energia']

    print(f"Você estava com {energia}⚡ de energia ! ")


    Jogada = jogaDADOS.jogaDados(dado)
    Jogada2 = jogaDADOS.jogaDados(dado)

    somaDados = Jogada + Jogada2


    print(F'\n🎲 : {Jogada}\n\n🎲 : {Jogada2}')
    
    print(f'A soma dos Dados é {somaDados}')

    EnergiaPerdida = somaDados

    energia = (energia - EnergiaPerdida)

    print(f'Agora Você perdeu {EnergiaPerdida} de energia⚡')
    print(f'Engergia Atual: {energia} ⚡')

    StatusAtuais['FolhaDeAventura']['energia'] = energia

    if energia > 0:
        return True
    else:
        return False


def ComparaHabilidade():

    global StatusAtuais

    habilidade = StatusAtuais['FolhaDeAventura']['habilidade']

    Jogada =jogaDADOS.jogaDados(dado)
    Jogada2 = jogaDADOS.jogaDados(dado)
                    
    print(f"Você esta com 👊 {habilidade} de habilidade! ")

    print(F'\n🎲 : {Jogada}\n\n🎲 : {Jogada2}')

    somaDados = Jogada + Jogada2

    if somaDados <= habilidade:
        print(f'soma de dados é : {somaDados} que é menor que sua habilidade : 👊 {habilidade} ')
        return True
    else:
        print(f'soma de dados maior que sua habilidade : 👊 {habilidade} ')
        return False


def PerdeEnergiaNoDado(multiplicador=None,maisum=None):
    Jogada = jogaDADOS.jogaDados(dado)
    
    global StatusAtuais

    print(F'\n🎲 : {Jogada}')
                    
    #perde energia
    energia = StatusAtuais['FolhaDeAventura']['energia']

    print('Energia anterior ⚡',energia)

    if multiplicador:
        energia -= (Jogada * multiplicador)
    elif maisum:
         energia -= Jogada + 1 
    else:
        energia -= Jogada

    StatusAtuais['FolhaDeAventura']['energia'] = energia

    print('Energia atual ⚡',energia)

    if energia <= 0:
        return False
    else:
        return True


def ComparaHabilidadeEEnergia():
    jogada = jogaDADOS.jogaDados(dado)
    jogada2 = jogaDADOS.jogaDados(dado)

    global StatusAtuais

    print(F'\n🎲 : {jogada}')
    print(F'\n🎲 : {jogada2}\n')

    total = jogada + jogada2
    
    energia = StatusAtuais['FolhaDeAventura']['energia']
    habilidade = StatusAtuais['FolhaDeAventura']['habilidade']

    print(f'Energia Atual:⚡{energia}')
    print(f'Habilidade Atual: 👊 {habilidade}')
    
    print(f'Total dos 🎲 Dados  : {total}  ')

    if total <= energia and total <= habilidade:
        return True
    
    else:
        return False


def Provisoes():
    global StatusAtuais

    provisao = StatusAtuais['FolhaDeAventura']['provisoes']
    energia = StatusAtuais['FolhaDeAventura']['energia']

    if provisao <= 0:
        print('Você não te mais provisões')
    else:
        print(f'\nProvisoes : {provisao}')
        print(f'Energia Atual ⚡{energia}')

        resposta = input(f'Quer usar provisão uma das {provisao} para recuperar 4 de energia? (Sim/Não)').lower()

        if resposta == 'sim':
            GanhaStatus(4,'energia','⚡')
            provisao -= 1                
            StatusAtuais['FolhaDeAventura']['provisoes'] = provisao
            energia = StatusAtuais['FolhaDeAventura']['energia']
            print(f'Provisoes atuais {provisao}\n')

        else:
            print('Provisão nao ultilizada.\n')


def PocaoEscolhida():
    global StatusAtuais
    
    pass


    # usarPocao = input(f'você deseja usar a sua poção escolhida {StatusAtuais["FolhaDeAventura"][]}').lower()

    # if usarPocao == 'sim':
    #     pass








################################################################################################
#################################################################################################
def Combate_294(nomeMonstro):

    # numero de rounds
    contadorBatalhas = 1

    #Valor do dano
    DanoCrítico = 4
    DanoCríticoP = 3
    DanoComum = 2
    DanoReduzido = 1

    # fazer o load do json com Status
    # with open(caminhoFolhaDeAventuraAtual,'r') as f:
    #     StatusGerais = json.load(f)

    global StatusAtuais

    # energia do personagem / criatura
    EnergiaPersonagem = StatusAtuais['FolhaDeAventura']['energia']
    EnergiaCriatura = StatusAtuais['EncontrosMonstros'][nomeMonstro]['energiaAtual']


    # enquanto ou a energia do personagem ou da criatura diferente de 0 continua a batalha
    while EnergiaPersonagem > 0 and EnergiaCriatura > 0: 

        input('\nVamos comçar o combate? Aperte ENTER para iniciar ')

        print('\n\n--------Início do Combate-----------')
        print(f'\nRound {contadorBatalhas}')
        print('\nPersonagem :')

        #Função que determina a força do personagem
        ForçaPersonagem = ForçaDeAtaque()

        print(f'\nForça do Personagem : 👊 {ForçaPersonagem}')
        print('------------------------------------------------')
            
        print(nomeMonstro)

        #Função que determina a força da criatura
        ForçaCriatura = ForçaDeAtaque(nomeMonstro)

        print(f'\nForça {nomeMonstro}: 👊 {ForçaCriatura}')
        print('------------------------------------------------')

        # Se a força for maior que da criatura : criatura perde pontos
        if ForçaPersonagem > ForçaCriatura:
            print('Você feriu a Criatura!😀\n')

            resposta = input('Você quer Testar sua sorte? (Sim/Não)').lower()

            if resposta == 'sim':

                testeSorte = Sorte()

                if testeSorte:
                    EnergiaCriatura -= DanoCrítico
                    print(f'Dano Crítico! -4 pontos de energia da {nomeMonstro}| Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')
                else:
                    EnergiaCriatura -= DanoReduzido
                    print(f'Dano reduzido! -1 ponto de energia | Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')

            else:
                 EnergiaCriatura -= DanoComum
                 print(f' {nomeMonstro} sofreu -2 pontos de energia | Energia atual⚡{EnergiaCriatura}')
                 print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')
                
            break



        # se a força for menor que da criatura, personagem perde pontos
        elif ForçaPersonagem < ForçaCriatura:
            print('Você foi ferido pela Criatura!😨')

            resposta = input('Você quer Testar sua sorte para ter chance de reduzir o dano? (Sim/Não)').lower()


            if resposta == 'sim':
                testeSorte = Sorte()

                if testeSorte:
                    EnergiaPersonagem -= DanoReduzido
                    print(f'Minimizou o ferimento! -1 pontos de energia do personagem | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')
                else:
                    EnergiaPersonagem -= DanoCríticoP
                    print(f'Ferimento grave! -3 ponto de energia | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')

            else:
                EnergiaPersonagem -= DanoComum
                print(f' Você sofreu -2 pontos de energia | Energia atual⚡{EnergiaPersonagem}')
                print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')


            # mando para json energia do personagem atualizada
            StatusAtuais['FolhaDeAventura']['energia'] = EnergiaPersonagem

           
            
        # se for igual, nao acontece nada
        elif ForçaPersonagem == ForçaCriatura:
            print('Golpé Neutralizado, forças iguais!')

        print('-------------------------------------------')
        
        contadorBatalhas +=1

    if EnergiaPersonagem > 0:
        return True

    else: 
        return False

def Combate_254(nomeMonstro):

    # numero de rounds
    contadorBatalhas = 0
    y = 0

    #Valor do dano
    DanoCrítico = 4
    DanoCríticoP = 3
    DanoComum = 2
    DanoReduzido = 1


    global StatusAtuais

    # energia do personagem / criatura
    EnergiaPersonagem = StatusAtuais['FolhaDeAventura']['energia']
    EnergiaCriatura = StatusAtuais['EncontrosMonstros'][nomeMonstro]['energiaAtual']


    # enquanto ou a energia do personagem ou da criatura diferente de 0 continua a batalha
    while EnergiaPersonagem > 0 and EnergiaCriatura > 0: 

        input('\nVamos comçar o combate? Aperte ENTER para iniciar ')

        print('\n\n--------Início do Combate-----------')
        print(f'\nRound {contadorBatalhas + 1}')
        print('\nPersonagem :')

        #Função que determina a força do personagem
        ForçaPersonagem = ForçaDeAtaque()

        print(f'\nForça do Personagem : 👊 {ForçaPersonagem}')
        print('------------------------------------------------')
            
        print(nomeMonstro)

        #Função que determina a força da criatura
        ForçaCriatura = ForçaDeAtaque(nomeMonstro)

        print(f'\nForça {nomeMonstro}: 👊 {ForçaCriatura}')
        print('------------------------------------------------')

        # Se a força for maior que da criatura : criatura perde pontos
        if ForçaPersonagem > ForçaCriatura:
            print('Você feriu a Criatura!😀\n')

            resposta = input('Você quer Testar sua sorte? (Sim/Não)').lower()

            if resposta == 'sim':

                testeSorte = Sorte()

                if testeSorte:
                    EnergiaCriatura -= DanoCrítico
                    print(f'Dano Crítico! -4 pontos de energia da {nomeMonstro}| Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')
                else:
                    EnergiaCriatura -= DanoReduzido
                    print(f'Dano reduzido! -1 ponto de energia | Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')

            else:
                 EnergiaCriatura -= DanoComum
                 print(f' {nomeMonstro} sofreu -2 pontos de energia | Energia atual⚡{EnergiaCriatura}')
                 print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')
                
        # se a força for menor que da criatura, personagem perde pontos
        elif ForçaPersonagem < ForçaCriatura:
            print('Você foi ferido pela Criatura!😨')

            resposta = input('Você quer Testar sua sorte para ter chance de reduzir o dano? (Sim/Não)').lower()


            if resposta == 'sim':
                testeSorte = Sorte()

                if testeSorte:
                    EnergiaPersonagem -= DanoReduzido
                    print(f'Minimizou o ferimento! -1 pontos de energia do personagem | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')
                else:
                    EnergiaPersonagem -= DanoCríticoP
                    print(f'Ferimento grave! -3 ponto de energia | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')

            else:
                EnergiaPersonagem -= DanoComum
                print(f' Você sofreu -2 pontos de energia | Energia atual⚡{EnergiaPersonagem}')
                print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')


            # mando para dicionario energia do personagem atualizada
            StatusAtuais['FolhaDeAventura']['energia'] = EnergiaPersonagem

           
            
        # se for igual, nao acontece nada
        elif ForçaPersonagem == ForçaCriatura:
            print('Golpé Neutralizado, forças iguais!')
            print('Que começe a próxima série de ataque!')

        print('-------------------------------------------')
        
        contadorBatalhas +=1

        if contadorBatalhas == 2:
            fuga = Fuga()

            if fuga:
                break

    #Se ele estiver vivo e decidir fugir
    if EnergiaPersonagem > 0 and fuga:
        y = 1
    
    #Se ele continuou e sobreviveu
    elif EnergiaPersonagem > 0:
        y = 2

    #Se ele morreu
    else: 
        y = 0
    
    return y

def Combate_327(nomeMonstro):
    # numero de rounds
    contadorBatalhas = 1
    y = 0

    #Valor do dano
    DanoCrítico = 4
    DanoCríticoP = 3
    DanoComum = 2
    DanoReduzido = 1

    
    global StatusAtuais
   

    # energia do personagem / criatura
    EnergiaPersonagem = StatusAtuais['FolhaDeAventura']['energia']
    EnergiaCriatura = StatusAtuais['EncontrosMonstros'][nomeMonstro]['energiaAtual']

    #Variável para controlar se criatura ganhou alguma série
    criatura_ganhou_serie = False

    # enquanto ou a energia do personagem ou da criatura diferente de 0 continua a batalha
    while EnergiaPersonagem > 0 and EnergiaCriatura > 0: 

        input('\nVamos comçar o combate? Aperte ENTER para iniciar ')

        print('\n\n--------Início do Combate-----------')
        print(f'\nRound {contadorBatalhas}')
        print('\nPersonagem :')

        #Função que determina a força do personagem
        ForçaPersonagem = ForçaDeAtaque()

        print(f'\nForça do Personagem : 👊 {ForçaPersonagem}')
        print('------------------------------------------------')
            
        print(nomeMonstro)


        #Função que determina a força da criatura
        ForçaCriatura = ForçaDeAtaque(nomeMonstro)

        print(f'\nForça {nomeMonstro}: 👊 {ForçaCriatura}')
        print('------------------------------------------------')

        # Se a força for maior que da criatura : criatura perde pontos
        if ForçaPersonagem > ForçaCriatura:
            print('Você feriu a Criatura!😀\n')

            resposta = input('Você quer Testar sua sorte? (Sim/Não)').lower()

            if resposta == 'sim':

                testeSorte = Sorte()

                if testeSorte:
                    EnergiaCriatura -= DanoCrítico
                    print(f'Dano Crítico! -4 pontos de energia da {nomeMonstro}| Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')
                else:
                    EnergiaCriatura -= DanoReduzido
                    print(f'Dano reduzido! -1 ponto de energia | Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')

            else:
                 EnergiaCriatura -= DanoComum
                 print(f' {nomeMonstro} sofreu -2 pontos de energia | Energia atual⚡{EnergiaCriatura}')
                 print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')

            
        # se a força for menor que da criatura, personagem perde pontos
        elif ForçaPersonagem < ForçaCriatura:
            print('Você foi ferido pela Criatura!😨')

            resposta = input('Você quer Testar sua sorte para ter chance de reduzir o dano? (Sim/Não)').lower()


            if resposta == 'sim':
                testeSorte = Sorte()


                if testeSorte:
                    EnergiaPersonagem -= DanoReduzido
                    print(f'Minimizou o ferimento! -1 pontos de energia do personagem | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')
                else:
                    EnergiaPersonagem -= DanoCríticoP
                    print(f'Ferimento grave! -3 ponto de energia | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')

            else:
                EnergiaPersonagem -= DanoComum
                print(f' Você sofreu -2 pontos de energia | Energia atual⚡{EnergiaPersonagem}')
                print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')


             # mando para dicionario energia do personagem atualizada
           
            StatusAtuais['FolhaDeAventura']['energia'] = EnergiaPersonagem
                 

            criatura_ganhou_serie = True
            break

            
        # se for igual, nao acontece nada
        elif ForçaPersonagem == ForçaCriatura:
            print('Golpé Neutralizado, forças iguais!')
            print('Que começe a próxima série de ataque!')

        print('-------------------------------------------')

        contadorBatalhas +=1

    #Se ele não perdeu nenhuma série
    if EnergiaPersonagem > 0:
        y = 1
    
    #Se ele predeu uma série, mas continua vivo
    elif EnergiaPersonagem > 0 and criatura_ganhou_serie:
        y = 2

    #Se ele morreu
    else: 
        y = 0
    
    return y



def Combate_escorpiao(nomeMonstro):

    # numero de rounds
    contadorBatalhas = 1

    #Valor do dano
    DanoCrítico = 4
    DanoCríticoP = 3
    DanoComum = 2
    DanoReduzido = 1

    # fazer o load do json com Status
    global StatusAtuais

    # energia do personagem / criatura
    EnergiaPersonagem = StatusAtuais['FolhaDeAventura']['energia']
    EnergiaCriatura = StatusAtuais['EncontrosMonstros'][nomeMonstro]['energia']


    # enquanto ou a energia do personagem ou da criatura diferente de 0 continua a batalha
    while EnergiaPersonagem > 0 and EnergiaCriatura > 0: 

        input('\nVamos começar o combate? Aperte ENTER para iniciar ')

        escolha = int(input("Escolha qual pinça vai atacar (1 ou 2)"))

        if escolha == 1:
            print("Você escolheu a pinça 1")
            
        else:
            print("Você escolheu a pinça 2")

        print('\n\n--------Início do Combate-----------')
        print(f'\nRound {contadorBatalhas}')
        print('\nPersonagem :')

        #Função que determina a força do personagem
        ForçaPersonagem = ForçaDeAtaque()

        print(f'\nForça do Personagem : 👊 {ForçaPersonagem}')
        print('------------------------------------------------')
            
        print(nomeMonstro)

        #Função que determina a força da criatura
        ForçaCriatura = ForçaDeAtaque(nomeMonstro)

        print(f'\nForça {nomeMonstro}: 👊 {ForçaCriatura}')
        print('------------------------------------------------')

        # Se a força for maior que da criatura : criatura perde pontos
        if ForçaPersonagem > ForçaCriatura:
            print('Você feriu a Criatura!😀\n')

            resposta = input('Você quer Testar sua sorte? (Sim/Não)').lower()

            if resposta == 'sim':

                testeSorte = Sorte()

                if testeSorte:
                    EnergiaCriatura -= DanoCrítico
                    print(f'Dano Crítico! -4 pontos de energia da {nomeMonstro}| Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')
                else:
                    EnergiaCriatura -= DanoReduzido
                    print(f'Dano reduzido! -1 ponto de energia | Energia atual {nomeMonstro}⚡{EnergiaCriatura}')
                    print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')

            else:
                 EnergiaCriatura -= DanoComum
                 print(f' {nomeMonstro} sofreu -2 pontos de energia | Energia atual⚡{EnergiaCriatura}')
                 print(f'Energia do Personagem : ⚡{EnergiaPersonagem}')

        # se a força for menor que da criatura, personagem perde pontos
        elif ForçaPersonagem < ForçaCriatura:
            print('Você foi ferido pela Criatura!😨')

            resposta = input('Você quer Testar sua sorte para ter chance de reduzir o dano? (Sim/Não)').lower()

            if resposta == 'sim':
                testeSorte = Sorte()

                if testeSorte:
                    EnergiaPersonagem -= DanoReduzido
                    print(f'Minimizou o ferimento! -1 pontos de energia do personagem | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')
                else:
                    EnergiaPersonagem -= DanoCríticoP
                    print(f'Ferimento grave! -3 ponto de energia | Energia atual⚡{EnergiaPersonagem}')
                    print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')

            else:
                EnergiaPersonagem -= DanoComum
                print(f' Você sofreu -2 pontos de energia | Energia atual⚡{EnergiaPersonagem}')
                print(f'Energia de {nomeMonstro}: ⚡{EnergiaCriatura}')

             # mando para json energia do personagem atualizada
           
            StatusAtuais['FolhaDeAventura']['energia'] = EnergiaPersonagem
                

        # se for igual, nao acontece nada
        elif ForçaPersonagem == ForçaCriatura:
            print('Golpé Neutralizado, forças iguais!')
            print('Que começe a próxima série de ataque!')

        print('-------------------------------------------')

        contadorBatalhas +=1

    if EnergiaPersonagem > 0:
         return True
    else:
         return False