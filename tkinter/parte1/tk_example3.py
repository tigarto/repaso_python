from tkinter import *
top = Tk()

def main():
    top['bg'] = 'light gray'
    Button(top, text="One").grid(row=0, column=0)
    Button(top, text="Two").grid(row=0, column=1, pady=10)
    Button(top, text="Three").grid(row=0, column=2)
    Button(top, text="Four").grid(row=1, column=2)
    Button(top, text="Five").grid(row=1, column=1)
    Button(top, text="Six").grid(row=1, column=0)
    mainloop()

main()