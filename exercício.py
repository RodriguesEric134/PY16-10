from tkinter import *


def muda_texto():
    num1["text"] + caixa_texto1.get()
    num2["text"] + caixa_texto2.get()



window = Tk()
window.title("Boas vindas")
window.geometry("490x200+400+200")

num1 = Label(window, text = "Numero1 ", font= "Impact 20 bold", pady=10) 
num1.pack(side=LEFT)

container1 = Frame(window, pady=15, padx=10)
container1.pack()

container2 = Frame(window, pady=15, padx=10)
container2.pack()

num2 = Label(container2, text="Numero 1", font="Impact 16", pady=10)
num2.pack(side=RIGHT)

caixa_texto1 = Entry(container1, font=("Times New Roman", "16"))
caixa_texto1.pack(side=RIGHT)

caixa_texto2 = Entry(container2, font=("Times New Roman", "16"))
caixa_texto2.pack(side=RIGHT)

botao = Button(window, text="Clique aqui", pady="15", padx="10", bg="black", fg="white")
botao["font"] = ("Courier New", "16", "bold")
botao["command"] = muda_texto
botao.pack()
caixa_texto1.focus()
caixa_texto2.focus()
window.mainloop()