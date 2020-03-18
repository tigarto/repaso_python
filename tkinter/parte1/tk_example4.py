
from tkinter import *
top = Tk()

def main():
    frame1 = Frame(top, bg = '#FFCCCC')
    frame1.pack(side=LEFT)
    Button(frame1, text="One", fg='red').grid(row=0,column=0)
    Button(frame1, text="Two").grid(row=0, column=1, pady=10)
    Button(frame1, text="Three").grid(row=0, column=2)
    frame2 = Frame(top, bg='cyan')
    frame2.pack(side='right')
    Button(frame2, text="Big Fat Four").pack(side=TOP)
    Button(frame2, text="Five").pack(side='top')
    Button(frame2, text="Six").pack(side='top',fill=BOTH)
    mainloop()

main()


