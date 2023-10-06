import jogaDADOS
import json

força = 0
provisoes = 10

def CriarPersonagem():


    def funcHabilidade():
        habilidade = jogadado1  + 6

        return habilidade
    
    def funcEnergia():
       energia = jogadado1 + jogadado2 + 12

       return energia
    
    def funcSorte():
        sorte = jogadado1  + 6

        return sorte
        
    dado = 0
   
    jogadado1 = jogaDADOS.jogaDados(dado)
    jogadado2 = jogaDADOS.jogaDados(dado)



    habilidade = funcHabilidade()

    energia = funcEnergia()

    sorte = funcSorte()

   


    DadosIniciais = {

        'habilidade': habilidade,
        'energia':energia,
        'sorte':sorte,
        'provisoes':provisoes

    }

    with open('D:/DadosPersonagem.json','w') as f:
        json.dump(DadosIniciais,f)
        


    print('jogada1',jogadado1)
    print('jogada2', jogadado2)
    print('habilidade', habilidade)
    print('energia' , energia)
    print('sorte', sorte)
    

    

