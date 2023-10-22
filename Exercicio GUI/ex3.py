#RM98297 Lucas Speranzini

from tkinter.ttk import *
from tkinter import *

def MudaImagem():

    dic = [
        {   
            'Escolha':0,
            'burger': 34.90,
            'noodles': 44.50,
            'pizza': 49
        },
        {   'Escolha':0,
            'fritas': 14.90,
            'nuggets': 9.50,
            'milho': 12.30
        },

        {   'Escolha':0,
            'Suco': 14.90,
            'Shake': 19.90
        }
    ]
       
    lanche = combo.get()
    porcao = combo2.get()
    bebida= combo3.get()

    valorTotal = 0

    if lanche:
        nova_imagem = "cardapio/" + combo.get() + '.png'
        imagem1['file'] = nova_imagem
        preçoLanche = dic[0][lanche]
        valorTotal += preçoLanche 
        

    if porcao:
        nova_imagem = "cardapio/" + combo2.get() + '.png'
        imagem2['file'] = nova_imagem
        preçoPorcao= dic[1][porcao]
        valorTotal += preçoPorcao
      

    if bebida:
        nova_imagem = "cardapio/" + combo3.get() + '.png'
        imagem3['file'] = nova_imagem
        preçoBebida= dic[2][bebida] 
        valorTotal += preçoBebida

    else:
        pass
        
    
    valor_total_label.config(text=f'Valor Total: R${valorTotal}')




fonte = ("Copper Black","14")

window = Tk()
window.geometry("500x500")

####################################
container1 = Frame(window)


labelLanche = Label(window, text='Lanche', font=fonte)
labelLanche.pack()

combo = Combobox(container1)
combo['values'] = ('Escolha','burger','noodles','pizza')
combo.current(0)
combo.pack()

container1.pack()
###################################

container2 = Frame(window, pady=5, padx=10)

labelPorcao = Label(window, text='Porcao', font=fonte)
labelPorcao.pack()


combo2 = Combobox(container2)
combo2['values'] = ('Escolha','fritas','nuggets','milho')
combo2.current(0)

combo2.pack()
container2.pack()
##########################################



container3 = Frame(window, pady=5, padx=10)

labelBebida = Label(window, text='Bebida', font=fonte)
labelBebida.pack()


combo3 = Combobox(container3)
combo3['values'] = ('Escolha','Suco','Shake',)
combo3.current(0)

combo3.pack()
container3.pack()
##############################################

containerImagem =  Frame(window, pady=40, padx=10)

imagem1 = PhotoImage(file='cardapio/escolha.png')
imagem2 = PhotoImage(file='cardapio/escolha.png')
imagem3 = PhotoImage(file='cardapio/escolha.png')

rotulo1 = Label(containerImagem, image=imagem1)
rotulo2 = Label(containerImagem, image=imagem2)
rotulo3 = Label(containerImagem, image=imagem3)

containerImagem.pack()
rotulo1.pack(side=LEFT)
rotulo2.pack(side=RIGHT)
rotulo3.pack(side=RIGHT)
###########################################

botao = Button(window, text='Fazer Pedido', pady=5, padx=10, font=fonte)

botao['command'] = MudaImagem
botao.pack()


###################################


valor_total_label = Label(window, text='', font=fonte)
valor_total_label.pack()




window.mainloop()