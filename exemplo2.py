from tkinter import *
window = Tk() #agora essa variavel pertence a biblioteca tk
window.title("Título da janela") #titulo
window.geometry("350x250+480+300") #altura e largura da janela + posições
window.configure(background="lightgreen")
rotulo = Label(window, font="Impact 20 bold", bg= "lightgreen") #define onde e o que será escrito na janela
rotulo.pack()
botao = Button(window, text="Click ME", padx=10)
botao["font"] = (("Times New Roman"), ("16"), ("bold"))
botao["fg"] = "white"
botao["bg"] = "black"
botao["command"] = window.quit
botao.pack() #compilador do "Rotulo"
window.mainloop() #rodar a janela em loop
