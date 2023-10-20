from tkinter.ttk import *
from tkinter import *

def MudaImagem():
    nova_imagem = "imagens/" + combo.get() + '.png'
    imagem['file'] = nova_imagem

fonte = ("Copper Black","14")

window = Tk()

window.title("Escolha seu Avatar")

window.geometry("400x300")


rotulo1 = Label(window, text='Escolha seu avatar', pady=20, font=fonte)
rotulo1.pack()

container1 = Frame(window, pady=20, padx=10)
container1.pack()

combo = Combobox(container1)
combo['values'] = ('arlequina','chaplin','gueixa','ninja','zorro')
combo['state'] = "readonly"
combo.current(0)
combo.pack(side=LEFT)

imagem = PhotoImage(file='imagens/arlequina.png')
rotulo2 = Label(container1, image=imagem)
rotulo2.pack(side=RIGHT)

botao = Button(window, text='Muda avatar', pady=5, padx=10, font=fonte)

botao['command'] = MudaImagem
botao.pack()

window.mainloop()