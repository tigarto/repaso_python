# secondTkinter.py

from tkinter import Label, Button, Tk

# The 'callback function' is invoked when the button is pressed.
def hello_callback(): 
    print ("Pateame!!!")

top = Tk()
# Make a Label.
l = Label(top, text = "My Button:")
l.pack()

# Make a button.
b = Button(top, text = "Hello", command = hello_callback)
b.pack()

top.mainloop()