from tkinter.ttk import *
from tkinter import *

def MudaImagem():

    dic = [

        lanche = {
            'burger':30,
            'noodles':10,
            'pizza':40
         },

       porcao = {
            'fritas':15,
            'nuggets':12,
            'milho':8
        },


        Bebida =  {
           'Suco',
           'Shake',
        }
    ]
       
    


    lanche = combo.get()
    porcao = combo2.get()
    bebida= combo3.get()

    if lanche:
        nova_imagem = "cardapio/" + combo.get() + '.png'
        imagem1['file'] = nova_imagem
        return PrecoLanche

    if porcao:
        nova_imagem = "cardapio/" + combo2.get() + '.png'
        imagem2['file'] = nova_imagem
        return PrecoPorcao

    if bebida:
        nova_imagem = "cardapio/" + combo3.get() + '.png'
        imagem3['file'] = nova_imagem
        return PrecoBebida
 


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



window.mainloop()