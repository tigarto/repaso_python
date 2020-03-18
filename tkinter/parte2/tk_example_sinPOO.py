from tkinter import *

# Funcionalidad (logica de la aplicación)
def eventoClick():
  print("Pateame!!!")

root = Tk() # Create a window
label = Label(root, text = "Welcome to Python") # Creando un label
button = Button(root, text = "Click Me", command = eventoClick) # Creando un boton
label.pack() # Colocando el label en la ventana raiz
button.pack() # Colocando el boton en la ventana raiz
root.mainloop()


