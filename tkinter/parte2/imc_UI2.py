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

class IMC_UI(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.imc = DoubleVar()
        self.pack()
          
        # Agregando los Frames
        self.fIn = LabelFrame(self, text = 'Entradas', width = 100, height = 100, relief = 'groove', borderwidth = 4)
        self.fInT = Frame(self.fIn)
        self.fInB = Frame(self.fIn)
        self.fCalc = Frame(self, width = 100, height = 100)

        # Agregando los widgets
        self.lw = Label(self.fInT, text = "Peso (kg): " , width = 14)
        self.lh = Label(self.fInB, text = "Altura (cm): ", width = 14 )
        self.eW = Entry(self.fInT, bd =5 )
        #self.eW["master"] = fInT
        #self.eW["bd"] = 5
        
        self.eH = Entry(self.fInB, bd =5)
        #self.eH["master"] = fInB
        #self.eH["bd"] = 5
        
        self.bIMC = Button(self.fCalc, text ="Calcular", command = self.calcular, padx = 10)
        self.eIMC = Entry(self.fCalc, textvariable = self.imc, bd =5)

        # Juntando evento por teclado
        self.eW.bind('<Return>',self.calc)
        self.eH.bind('<Return>',self.calc)

        # Ubicando los layouts y widgets en la ventana
        self.fIn.pack(padx = 5, pady = 5, side = 'top')
        self.fInT.pack()
        self.fInB.pack()
        self.fCalc.pack(fill=X, padx=5, pady=5)
        self.lw.pack(side = LEFT)
        self.eW.pack(side = RIGHT)
        self.lh.pack(side = LEFT)
        self.eH.pack(side = RIGHT)
        self.bIMC.pack(side = LEFT)
        self.eIMC.pack(side = RIGHT)
        self.eIMC.configure(state = DISABLED) 

    def calcular(self):
        print ("Boton presionado")
        if not( ):
            p = float(self.eW.get())
            h = float(self.eH.get())
            imcO = IMC(h,p)
            self.imc.set(imcO.calcIMC())
            print ("IMC =",self.imc.get())
        
    def calc(self, event):    
        if self.eW.get() == '' or self.eH.get() == '':
            print ("Faltan argumentos")
        else:
            print ("Se puede proceder a realizar el calculo")
            self.calcular() 



root = Tk()
app = IMC_UI(master=root) # Instantiating the App class
app.master.title("Sample application") # Sets the title of the window
app.mainloop() # Starts the app's main loop; waiting for mouse and keyboard events

'''
Referencias: 
http://effbot.org/tkinterbook/widget.htm#Tkinter.Widget.winfo_children-method
https://stackoverflow.com/questions/7290071/getting-every-child-widget-of-a-tkinter-window
'''