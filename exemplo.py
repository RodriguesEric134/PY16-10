from tkinter import *
window = Tk() #agora essa variavel pertence a biblioteca tk
window.title("Título da janela") #titulo
window.geometry("350x250+480+300") #altura e largura da janela + posições
window.configure(background="lightgreen")
rotulo = Label(window) #define onde e o que será escrito na janela
rotulo["text"] = "Hello World"
rotulo["font"] = ("impact", "20", "bold")
rotulo["fg"] = "brown"
rotulo["bg"] = "lightgreen"
rotulo["pady"] = 5
rotulo["padx"] = 10
rotulo["width"] = 20
rotulo["anchor"] = "w"
rotulo.pack() #compilador do "Rotulo"
window.mainloop() #rodar a janela em loop
