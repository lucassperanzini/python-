import jogaDADOS
import json


dado = 0
provisoes = 10


caminhoFolhaDeAventura = 'D:/DadosPersonagemInicial.json'
caminhoFolhaDeAventuraAtual = 'D:/DadosPersonagemAtual.json'


#Função para criar os status do personagem
def CriarPersonagem():


    def funcHabilidade():
        habilidade = JogaDado  + 6

        return habilidade
    
    def funcEnergia():
       energia = JogaDado + JogaDado2 + 12

       return energia
    
    def funcSorte():
        sorte = JogaDado + 6

        return sorte
        
   
    JogaDado = jogaDADOS.jogaDados(dado)
    JogaDado2 = jogaDADOS.jogaDados(dado)


    # dicionario que guarda Status do personagem
    StatusIniciais = {

        'FolhaDeAventura':{
            'habilidade': funcHabilidade(),
            'energia':funcEnergia(),
            'sorte':funcSorte(),
            'provisoes':provisoes
        }
        

    }

    #mandando o dicionario com o status para json imutável(inicial)
    with open(caminhoFolhaDeAventura,'w') as f:
        json.dump(StatusIniciais,f)

    # mandando dicionario com status inicial que mudará durante a partida
    with open(caminhoFolhaDeAventuraAtual,'w') as f:
        json.dump(StatusIniciais,f)
        

    # print das informações do dicionario
    print('\n-------------------INFORMAÇÕES INICIAIS--------------------------')
    print(f'\n    Dado1 : {JogaDado}\n')
    print(f'    Dado2 : {JogaDado2}\n')
    print(f'''   Habilidade : {StatusIniciais['FolhaDeAventura']['habilidade']}
          
    Energia : {StatusIniciais['FolhaDeAventura']['energia']}

    Sorte: {StatusIniciais['FolhaDeAventura']['sorte']}

    Provisões: {StatusIniciais['FolhaDeAventura']['provisoes']} 
--------------------------------------------------------------------------------
''')
    


def criarCriatura(habilidade,energia,nomeMonstro):

    #LOAD em todo o json personagem/ vai cria criatura
    with open(caminhoFolhaDeAventuraAtual, 'r') as f:
         StatusIniciaisCriatura = json.load(f)

    # SE nao encontra a chave dentro do json, vai cria uma chave EncontrosMonstros
    if 'EncontrosMonstros' not in StatusIniciaisCriatura:
         StatusIniciaisCriatura['EncontrosMonstros'] = {}
    
    

    # Dentro da chave EncontrosMonstros vou criar a key 'nome monstro' e add suas caractertisticas
    StatusIniciaisCriatura['EncontrosMonstros'][nomeMonstro] = {

            'habilidade':habilidade ,
            'energia':energia,
           

         }
    
    

    # Enviando para folha de aventura as informações da criatura
    with open(caminhoFolhaDeAventuraAtual,'w') as f:
         json.dump(StatusIniciaisCriatura,f)


#funcao para medir força de ataque de acordo com a habilidade, verificando quem tem mais força
def ForçaDeAtaque(Caminho,setor,nomeMonstro=None):
        
        Jogada = jogaDADOS.jogaDados(dado)
        Jogada2 = jogaDADOS.jogaDados(dado)


        print(F'\n🎲 : {Jogada}\n\n🎲 : {Jogada2}')


        with open(Caminho,'r') as f:
          Status = json.load(f)

        #verificacao se quando eu chamar funcao tiver nome monstro como parametro a força sera da criatura
        #se nao a funcao sera para o personagem
        if nomeMonstro:
            força = Status[setor][nomeMonstro]['habilidade'] + (Jogada + Jogada2)
        else:
            força = Status[setor]['habilidade'] + (Jogada + Jogada2)

        return força

def Fuga():
    #pode escapar de um combate
    # perde -2 de energia por ser covarde
    #pode usar sorte no ferimento
    # so pode fugir de acordo com instruções específicas
    pass

def Sorte():
    tiveSorte = False

    #Jogada dados
    Jogada = jogaDADOS.jogaDados(dado)
    Jogada2 = jogaDADOS.jogaDados(dado)

    #Load do json com todos Status
    with open(caminhoFolhaDeAventuraAtual,'r') as f:
        StatusGerais = json.load(f)

    Sorte = StatusGerais['FolhaDeAventura']['sorte']


    print('Vamos ver se você tem sorte ou não!!')
    print(f'Sorte Atual: {Sorte}')

    print(F'\n🎲 : {Jogada}\n\n🎲 : {Jogada2}')


    somaDados = Jogada + Jogada2

    if somaDados <= Sorte:
        tiveSorte = True
        print('\nResultado favorável!Teve sorte')
    else:
        tiveSorte = False
        print('\nPerdeu haha nao foi dessa vez!')
        print('Você Sofrerá as consequências!')


    StatusGerais['FolhaDeAventura']['sorte'] = Sorte - 1

    with open(caminhoFolhaDeAventuraAtual,'w') as f:
        json.dump(StatusGerais,f)

    print(f'\nComo usou o recurso Sorte perde 1 ponto | Sorte ATUAL: {StatusGerais["FolhaDeAventura"]["sorte"]} ')


    #Retorna True ou False se ele teve sorte
    return tiveSorte
    
def Combate(nomeMonstro):
    #USo da sorte no combate IMPLEMENTAR

    # numero de rounds
    contadorBatalhas = 1

    # fazer o load do json com Status
    with open(caminhoFolhaDeAventuraAtual,'r') as f:
        StatusGerais = json.load(f)

    # energia do personagem / criatura
    EnergiaPersonagem = StatusGerais['FolhaDeAventura']['energia']
    EnergiaCriatura = StatusGerais['EncontrosMonstros'][nomeMonstro]['energia']


    # enquanto ou a energia do personagem ou da criatura diferente de 0 continua a batalha
    while EnergiaPersonagem > 0 and EnergiaCriatura > 0: 

        input('\nVamos comçar o combate? Aperte ENTER para iniciar ')

        print('\n\n--------Início do Combate-----------')
        print(f'\nRound {contadorBatalhas}')
        print('\nPersonagem :')

        #Função que determina a força do personagem
        ForçaPersonagem = ForçaDeAtaque(caminhoFolhaDeAventuraAtual,'FolhaDeAventura')

        print(f'\nForça do Personagem : {ForçaPersonagem}')
        print('------------------------------------------------')
            
        print(nomeMonstro)

        #Função que determina a força da criatura
        ForçaCriatura = ForçaDeAtaque(caminhoFolhaDeAventuraAtual,'EncontrosMonstros',nomeMonstro)

        print(f'\nForça Criatura: {ForçaCriatura}')
        print('------------------------------------------------')

        # Se a força for maior que da criatura : criatura perde pontos
        if ForçaPersonagem > ForçaCriatura:
            print('Você feriu a Criatura!😀\n')

            EnergiaCriatura -= 2


            #energia perdida, vou mandar para o json dados atualizados da energia
            with open(caminhoFolhaDeAventuraAtual,'w') as f:
                StatusGerais['EncontrosMonstros'][nomeMonstro]['energia'] -= 2
                json.dump(StatusGerais,f)


            print(f'Criatura perdeu 2 pontos de Energia, energia atual : {EnergiaCriatura}') 

        # se a força for menor que da criatura, personagem perde pontos
        elif ForçaPersonagem < ForçaCriatura:
            print('Você foi ferido pela Criatura!😨')

            EnergiaPersonagem -= 2

            # mando para json energia do personagem atualizada
            with open(caminhoFolhaDeAventuraAtual,'w') as f:
                StatusGerais['FolhaDeAventura']['energia'] -= 2
                json.dump(StatusGerais,f)

           
            print(f'Você perdeu 2 pontos de Energia, energia atual : {EnergiaPersonagem}')

    
            
        # se for igual, nao acontece nada
        elif ForçaPersonagem == ForçaCriatura:
            print('Golpé Neutralizado, forças iguais!')
            print('Que começe a próxima série de ataque!')

        print('-------------------------------------------')
        
        contadorBatalhas +=1

    

    
    if EnergiaPersonagem > EnergiaCriatura:
        return True
    else:
        return False

          
############# Funções específicas da história ###############################

def AranhaPerigosa():
    with open(caminhoFolhaDeAventuraAtual,'r') as f:
        StatusGerais = json.load(f) 
                    
    #perde habilidade
    energia = StatusGerais['FolhaDeAventura']['energia']

    print('Energia anterior',energia)

    energia -= 6

    StatusGerais['FolhaDeAventura']['energia'] = energia

    with open(caminhoFolhaDeAventuraAtual,'w') as f:
        json.dump(StatusGerais,f)

    if energia <= 0:
        print('Acabou sua energia! Você perdeu')

    else:
        print('Você sobreviveu a Aranha VIUVA NEGRA')
        print('energia atual',energia)

 
        


def PerdeHabilidade(valor):
    with open(caminhoFolhaDeAventuraAtual,'r') as f:
        StatusGerais = json.load(f) 
                    
    #perde habilidade
    habilidade = StatusGerais['FolhaDeAventura']['habilidade']

    print('Habilidade anterior',habilidade)

    habilidade -= valor

    StatusGerais['FolhaDeAventura']['habilidade'] = habilidade

    print('Habilidade atual',habilidade)

    with open(caminhoFolhaDeAventuraAtual,'w') as f:
        json.dump(StatusGerais,f)







