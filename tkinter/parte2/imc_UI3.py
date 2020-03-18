#test.py
try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import pygubu

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

class Application:
    def __init__(self, master):
        self.imc = tk.DoubleVar()

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('imc_UI3.ui')
        
        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainWindow', master)
        
        # Create check button object
        self.eW = builder.get_object('eW', self.mainwindow)
        self.eH = builder.get_object('eH', self.mainwindow)
        self.eIMC = builder.get_object('eIMC', self.mainwindow)
        self.eIMC["textvariable"] = self.imc

        # Juntando evento por teclado
        self.eW.bind('<Return>',self.calc)
        self.eH.bind('<Return>',self.calc)


        #4: Connect callbacks
        builder.connect_callbacks(self)

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
        


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()