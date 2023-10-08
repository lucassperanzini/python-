import jogaDADOS
import json


dado = 0
provisoes = 10


caminhoFolhaDeAventura = 'D:/DadosPersonagemInicial.json'
caminhoFolhaDeAventuraAtual = 'D:/DadosPersonagemAtual.json'



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
    
    

    # Dentro da chave EncontrosMonstros vou adicionar a key 'nome monstro' e add suas caractertisticas
    StatusIniciaisCriatura['EncontrosMonstros'][nomeMonstro] = {

            'habilidade':habilidade ,
            'energia':energia,
           

         }
    
    

    # Enviando para folha de aventura as informações das criaturas
    with open(caminhoFolhaDeAventuraAtual,'w') as f:
         json.dump(StatusIniciaisCriatura,f)


def ForçaDeAtaque(Caminho,setor,nomeMonstro=None):
        
        Jogada = jogaDADOS.jogaDados(dado)
        Jogada2 = jogaDADOS.jogaDados(dado)


        print(F'\n 🎲 : {Jogada}\n\n🎲 : {Jogada2}')


        with open(Caminho,'r') as f:
          Status = json.load(f)

        if nomeMonstro:
            força = Status[setor][nomeMonstro]['habilidade'] + (Jogada + Jogada2)
        else:
            força = Status[setor]['habilidade'] + (Jogada + Jogada2)

        return força
    
def Combate(nomeMonstro):

    with open(caminhoFolhaDeAventuraAtual,'r') as f:
        StatusGerais = json.load(f)

    EnergiaPersonagem = StatusGerais['FolhaDeAventura']['energia']
    EnergiaCriatura = StatusGerais['EncontrosMonstros'][nomeMonstro]['energia']

    
    while EnergiaPersonagem > 0 and EnergiaCriatura > 0: 

        print('--------Início do Combate-----------')
        print('\nPersonagem :')

        ForçaPersonagem = ForçaDeAtaque(caminhoFolhaDeAventuraAtual,'FolhaDeAventura')

        print(f'\nForça do Personagem : {ForçaPersonagem}')
        print('------------------------------------------------')
            
        print('Criatura')

        ForçaCriatura = ForçaDeAtaque(caminhoFolhaDeAventuraAtual,'EncontrosMonstros',nomeMonstro)

        print(f'\nForça Criatura: {ForçaCriatura}')
        print('------------------------------------------------')

        if ForçaPersonagem > ForçaCriatura:
            print('Você feriu a Criatura!😀\n')

            EnergiaCriatura -= 2

            with open(caminhoFolhaDeAventuraAtual,'w') as f:
                StatusGerais['EncontrosMonstros'][nomeMonstro]['energia'] -= 2
                json.dump(StatusGerais,f)


            print(f'Criatura perdeu 2 pontos de Energia, energia atual : {EnergiaCriatura}')

           

                
        elif ForçaPersonagem < ForçaCriatura:
            print('Você foi ferido pela Criatura!😨')

            EnergiaPersonagem -= 2

            with open(caminhoFolhaDeAventuraAtual,'w') as f:
                StatusGerais['FolhaDeAventura']['energia'] -= 2
                json.dump(StatusGerais,f)


            print(f'Você perdeu 2 pontos de Energia, energia atual : {EnergiaPersonagem}')

            
            

        elif ForçaPersonagem == ForçaCriatura:
            print('Golpé Neutralizado, forças iguais!')
            print('Que começe a próxima série de ataque!')

          


 
        












