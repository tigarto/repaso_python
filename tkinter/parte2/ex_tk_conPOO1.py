from tkinter import Label, Button,Tk

class MyApp:
    def __init__ (self, master):
        self.l = Label(master,text = "My Button:")
        self.l.pack()
        self.b = Button(master, text = "Hello", command = self.hello)
        self.b.pack()
        
    # Function called when the button  is pressed.
    def hello(self): 
        print ("Pateame!!!!")


top = Tk()
# Note that the constructor takes the parent window as an argument.
app = MyApp(top)
top.mainloop()