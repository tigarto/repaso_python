from tkinter import *


class UIPateame(Frame):
  def __init__(self,master = None):
    Frame.__init__(self, master)
    # Instanciando los widgets
    self.label = Label(self,text = "Welcome to Python") # Creando un label
    self.button = Button(self, text = "Click Me", command = self.eventoClick) # Creando un boton
    # Colocando los widgets en la interfaz
    self.pack()
    self.label.pack()
    self.button.pack()
  def eventoClick(self):
    print("Pateame!!!")


# Allow the class to run stand-alone.
if __name__ == "__main__":
    app = UIPateame()
    app.mainloop()

