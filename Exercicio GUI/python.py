from tkinter.ttk import *
from tkinter import *

window = Tk()

window.title('Imagem na janela')

imagem = PhotoImage(file='imagens/batman.png')

rotulo = Label(window, image=imagem)

rotulo.pack()
window.mainloop()