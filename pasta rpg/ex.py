import jogaDADOS
import json

dado = 0
força = 0
provisoes = 10



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

        'habilidade': funcHabilidade(),
        'energia':funcEnergia(),
        'sorte':funcSorte(),
        'provisoes':provisoes

    }

    with open('D:/DadosPersonagem.json','w') as f:
        json.dump(StatusIniciais,f)
        

    print('\n-------------------INFORMAÇÕES INICIAIS--------------------------')
    print(f'\n    Dado1 : {JogaDado}\n')
    print(f'    Dado2 : {JogaDado2}\n')
    print(f'''   Habilidade : {StatusIniciais['habilidade']}
          
    Energia : {StatusIniciais['energia']}

    Sorte: {StatusIniciais['sorte']}

    Provisões: {StatusIniciais['provisoes']} 
--------------------------------------------------------------------------------
''')
    


def criarCriatura(habilidade,energia):


    StatusIniciaisCriatura = {

        'habilidade':habilidade ,
        'energia':energia,

    }

    with open('D:/DadosCriatura.json','w') as f:
         json.dump(StatusIniciaisCriatura,f)


def ForçaDeAtaque(Caminho):
        
        Jogada = jogaDADOS.jogaDados(dado)
        Jogada2 = jogaDADOS.jogaDados(dado)


        print(F'\n 🎲 : {Jogada}\n\n🎲 : {Jogada2}')



        # Atualizar a habilidade de acordo com a soma dos dados ( habilidade)
        with open(Caminho,'r') as f:
          Status = json.load(f)


        força = Status['habilidade'] + (Jogada + Jogada2)

        return força
    
def Combate():

    # with open('D:/DadosPersonagem.json','r') as f:
    #     StatusAtualP = json.load(f)

    # energiaPersonagem = StatusAtualP['energia']

    # with open('D:/DadosCriatura.json','r') as f:
    #     StatusAtualC = json.load(f)

    # energiaCriatura  = StatusAtualC['energia']
    

    # while energiaPersonagem or energiaCriatura != 0:

    #     print(energiaPersonagem,energiaCriatura)

    print('--------Início do Combate-----------')
    print('\nPersonagem :')

    ForçaPersonagem = ForçaDeAtaque('D:/DadosPersonagem.json')

    print(f'\nForça do Personagem : {ForçaPersonagem}')
    print('------------------------------------------------')
        
    print('Criatura')

    ForçaCriatura = ForçaDeAtaque('D:/DadosCriatura.json')

    print(f'\nForça Criatura: {ForçaCriatura}')
    print('------------------------------------------------')

    if ForçaPersonagem > ForçaCriatura:
        print('Você feriu a Criatura!😀\n')

        with open('D:/DadosCriatura.json','r') as f:
            StatusCriatura = json.load(f)

        StatusCriatura['energia'] -= 2

        with open('D:/DadosCriatura.json','w') as f:
            json.dump(StatusCriatura,f)


        print(f'Criatura perdeu 2 pontos de Energia, energia atual : {StatusCriatura["energia"]}')

            
    elif ForçaPersonagem < ForçaCriatura:
        print('Você foi ferido pela Criatura!😨')

        with open('D:/DadosPersonagem.json','r') as f:
            Status = json.load(f)

        Status['energia'] -= 2

        with open('D:/DadosPersonagem.json','w') as f:
            json.dump(Status,f)
           

        print(f'Você perdeu 2 pontos de Energia, energia atual : {Status["energia"]}')
        

    elif ForçaPersonagem == ForçaCriatura:
        print('Golpé Neutralizado, forças iguais!')

 
        












