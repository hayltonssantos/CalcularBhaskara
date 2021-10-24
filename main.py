from tkinter import * 
from math import *

#agora vou por a função, ja tenho pronta rs
def baskara(a,b,c):
    a = int(a.get())
    b = int(b.get())
    c = int(c.get())

    delta = ((b*b)-(4*a*c))
    raiz = sqrt(delta)

    lb_delta.configure(text=f'\n**PASSO A PASSO DELTA**\n Δ = b² - 4ac\nΔ = {b*b} - 4.{a}.({c})\nΔ = {b*b} - {4*a*c}\nΔ = {((b*b)-(4*a*c))}\n')
    lb_x.configure(text=f'\n****PASSO A PASSO X****\nx = -b ± √Δ / 2.a\nx = {b*(-1)} ± √{delta} / 2.{a}\nx = {b*(-1)} ± {raiz} / {2*a}')
    lb_x1.configure(text=f'\n****PASSO A PASSO X1****\n-b + √Δ / 2.a\nx¹ = {b*(-1)} + √{delta} / 2.{a}\nx¹ = {b*(-1)} + {raiz} / {2*a}\nx¹ = {((b*(-1)) + (raiz))} / {2*a}\nx¹ = {(((b*(-1)) + (raiz))) / (2*a)}\n')
    lb_x2.configure(text=f'\n***PASSO A PASSO X2***\n-b - √Δ / 2.a\nx² = {b*(-1)} - √{delta} / 2.{a}\nx² = {b*(-1)} - {raiz} / {2*a}\nx² = {((b*(-1)) - (raiz))} / {2*a}\nx² = {(((b*(-1)) - (raiz))) / (2*a)}')

#estas definiçoes em baixo são da tela
root = Tk()
root.title("Calcular Baskara")
root.geometry("600x600")
root.configure(background="#117a37")

#variaveis
v_a = StringVar()
v_b = StringVar()
v_c = StringVar()

#labels, inputs

lb_a = Label(root,text="Valor de A ->")
lb_b = Label(root,text="Valor de B ->")
lb_c = Label(root,text="Valor de C ->")

#esses valores vazios, serão alterados após
#resultado de baskara e seu passo a passo
lb_delta = Label(root, text="")
lb_x = Label(root, text="")
lb_x1 = Label(root, text="")
lb_x2 = Label(root, text="")

#inputs para receber os dados
input_a = Entry(root, textvariable=v_a)
input_b = Entry(root, textvariable=v_b)
input_c = Entry(root, textvariable=v_c)

bt_calc = Button(text="Calcular", command= lambda: baskara(v_a,v_b,v_c))

#labels na tela com posição em pixels 
lb_a.place(x=100,y= 100)
lb_b.place(x=100, y=140)
lb_c.place(x=100,y=180)

input_a.place(x=190, y=100, width=30, height=20)
input_b.place(x=190, y=140, width=30, height=20)
input_c.place(x=190, y=180, width=30, height=20)
lb_delta.place(x=100, y=260)
lb_x.place(x=290, y=280)
lb_x1.place(x=100, y=390)
lb_x2.place(x=290, y=390)

bt_calc.place(x=100, y=220)


root.mainloop()