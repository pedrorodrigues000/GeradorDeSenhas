from calendar import c
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import string
import random

cor1 = '#444466'  # preto
cor2 = '#feffff'  # branco
cor3 = '#f05a43'  # vermelho

window = Tk()
window.title('')
window.geometry('295x350')
window.configure(bg=cor2)

estilo = ttk.Style(window)
estilo.theme_use('clam')

# divisão da tela
frame_nomeApp = Frame(window, width=295, height=50, bg=cor2, padx=0, relief='flat')
frame_nomeApp.grid(row=0, column=0, sticky=NSEW)

frame_corpo = Frame(window, width=295, height=310, bg=cor2, padx=0, relief='flat')
frame_corpo.grid(row=1, column=0, sticky=NSEW)

# frame nomeAPP

img = Image.open('senha.png')
img = img.resize((40, 40), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_nomeApp, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor2)
app_logo.place(x=2, y=0)

app_nome = Label(frame_nomeApp, text='GERADOR DE SENHAS', height=1, width=20 , padx=0, font=('Ivy 16 bold'),relief='flat', anchor='nw', bg=cor2, fg=cor1)
app_nome.place(x=45, y=5)

app_linha = Label(frame_nomeApp, text='', height=1, width=295 , padx=0, font=('Ivy 1'),relief='flat', anchor='nw', bg=cor3, fg=cor3)
app_linha.place(x=0, y=43)

# função gerar senha

def gerar_senha():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '0123456789'
    simbolos = '-_!@#$%'
    
    global combinar
    
    if estado1.get() == alfabeto_maior:
        combinar += alfabeto_maior
    else:
        pass
    
    if estado2.get() == alfabeto_menor:
        combinar += alfabeto_menor
    else:
        pass
    
    if estado3.get() == numeros:
        combinar += numeros
    else:
        pass
    
    if estado4.get() == simbolos:
        combinar += simbolos
    else:
        pass
    
    c = int(spin.get())
    senha = ''.join(random.sample(combinar, c))
    
    print(senha)
    
    


# label 1 frame corpo

app_senha = Label(frame_corpo, text='- - - -', height=1, width=22 , padx=0, font=('Ivy 12 bold'),relief='solid', anchor='center', bg=cor2, fg=cor1)
app_senha.grid(row=0, column=0, sticky=NSEW, columnspan=1, padx=3, pady=10)

app_info = Label(frame_corpo, text='Número total de caracteres', height=1, padx=0, font=('Ivy 10 bold'),relief='flat', anchor='nw', bg=cor2, fg=cor1)
app_info.grid(row=1, column=0, sticky=NSEW, columnspan=2, padx=5, pady=1 )

var = IntVar()
var.set(6)
spin = Spinbox(frame_corpo, from_ = 0, to = 20, width=5, textvariable=var)
spin.grid(row=2, column=0, sticky=NW, columnspan=1, padx=5, pady=8)

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '0123456789'
simbolos = '-_!@#$%'

frame_caracteres = Frame(frame_corpo, width=295, height=210, bg=cor2, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# ------ letra maiúscula -----

estado1 = StringVar()
estado1.set(False)

check1 = Checkbutton(frame_caracteres, width=1, var = estado1, onvalue=alfabeto_maior, offvalue='off', relief='flat', bg=cor2)
check1.grid(row=0, column=0, sticky=NW, padx=2, pady=5 )

letra_maior = Label(frame_caracteres, text='ABC Letras maiúsculas', height=1, padx=0, font=('Ivy 10 bold'),relief='flat', anchor='nw', bg=cor2, fg=cor1)
letra_maior.grid(row=0, column=1, sticky=NW, padx=2, pady=5 )

# ------ letra minúscula ----- 

estado2 = StringVar()
estado2.set(False)

check2 = Checkbutton(frame_caracteres, width=1, var = estado2, onvalue=alfabeto_menor, offvalue='off', relief='flat', bg=cor2)
check2.grid(row=1, column=0, sticky=NW, padx=2, pady=5 )

letra_menor = Label(frame_caracteres, text='abc Letras minúscula', height=1, padx=0, font=('Ivy 10 bold'),relief='flat', anchor='nw', bg=cor2, fg=cor1)
letra_menor.grid(row=1, column=1, sticky=NSEW, columnspan=2, padx=5, pady=1 )

# ------ letra minúscula -----
estado3 = StringVar()
estado3.set(False)

check3 = Checkbutton(frame_caracteres, width=1, var = estado3, onvalue=numeros, offvalue='off', relief='flat', bg=cor2)
check3.grid(row=2, column=0, sticky=NW, padx=2, pady=5 )

letra_maior = Label(frame_caracteres, text='123 Números', height=1, padx=0, font=('Ivy 10 bold'),relief='flat', anchor='nw', bg=cor2, fg=cor1)
letra_maior.grid(row=2, column=1, sticky=NW, padx=2, pady=5 )

# ------ letra minúscula -----

estado4 = StringVar()
estado4.set(False)

check4 = Checkbutton(frame_caracteres, width=1, var = estado4, onvalue=simbolos, offvalue='off', relief='flat', bg=cor2)
check4.grid(row=3, column=0, sticky=NW, padx=2, pady=5 )

letra_maior = Label(frame_caracteres, text='!@# Símbolos', height=1, padx=0, font=('Ivy 10 bold'),relief='flat', anchor='nw', bg=cor2, fg=cor1)
letra_maior.grid(row=3, column=1, sticky=NW, padx=2, pady=5 )

# Botão

botao_senha = Button(frame_caracteres, command=gerar_senha ,text='Gerar Senha', width=30, height=1, padx=0, overrelief='solid' ,font=('Ivy 10 bold'),relief='flat', anchor='center', bg=cor3, fg=cor2)
botao_senha.grid(row=4, column=0, sticky=NSEW, padx=25, pady=11,columnspan=3 )

botao_copiar = Button(frame_corpo, text='Copiar', width=6, height=1, padx=0, overrelief='solid' ,font=('Ivy 10 bold'),relief='flat', anchor='center', bg=cor3, fg=cor2)
botao_copiar.grid(row=0, column=1, sticky=NW, columnspan=1, padx=3, pady=10)



window.mainloop()
