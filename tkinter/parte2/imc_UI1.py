# -*- coding: utf-8 -*-

from tkinter import *

class IMC:
    def __init__(self, h = 0,w = 0):
        self.heigh = h/100.0
        self.weigh = w
    def calcIMC(self):
        if self.heigh != 0:
            IMC = (self.weigh)/float(self.heigh**2)
        else:
            IMC = 0
        return IMC

top = Tk()
top.title("Calculadora IMC")
imc = DoubleVar()

def calc(event):    
    if eW.get() == '' or eH.get() == '':
        print ("Faltan argumentos")
    else:
        print ("Se puede proceder a realizar el calculo")
        calcular()

def calcular():
    global imc
    print ("Boton presionado")
    if not( ):
        p = float(eW.get())
        h = float(eH.get())
        imcO = IMC(h,p)
        imc.set(imcO.calcIMC())
        print ("IMC =",imc.get())

# Frames
fIn = LabelFrame(top, text = 'Entradas', width = 100, height = 100, relief = 'groove', borderwidth = 4)
fInT = Frame(fIn)
fInB = Frame(fIn)
fCalc = Frame(top, width = 100, height = 100)

# Code to add
lw = Label(fInT, text = "Peso (kg): " , width = 14)
lh = Label(fInB, text = "Altura (cm): ", width = 14 )
eW = Entry(fInT, bd =5)
eH = Entry(fInB, bd =5)
bIMC = Button(fCalc, text ="Calcular", command = calcular, padx = 10)
eIMC = Entry(fCalc, textvariable = imc, bd =5)

# Juntando evento por teclado
eW.bind('<Return>',calc)
eH.bind('<Return>',calc)

fIn.pack(padx = 5, pady = 5, side = 'top')
fInT.pack()
fInB.pack()
fCalc.pack(fill=X, padx=5, pady=5)
lw.pack(side = LEFT)
eW.pack(side = RIGHT)
lh.pack(side = LEFT)
eH.pack(side = RIGHT)
bIMC.pack(side = LEFT)
eIMC.pack(side = RIGHT)
eIMC.configure(state = DISABLED) 
top.resizable(width=FALSE, height=FALSE)
#mainloop
top.mainloop()