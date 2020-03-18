from tkinter import Label, Button, Frame

# Extend the Frame class, to inherit the mainloop function.

class MyApp(Frame):
    def __init__ (self, master = None):
        # Construct the Frame object.
        Frame.__init__(self, master)
        self.pack()
        self.l = Label(self,text = "My Button:")
        self.l.pack()
        self.b = Button(self,text = "Hello",command = self.hello)
        self.b.pack()
    
    # Function called when the button is pressed.
    def hello(self): 
        print ("Pateame!!!")

# Allow the class to run stand-alone.
if __name__ == "__main__":
    MyApp().mainloop()