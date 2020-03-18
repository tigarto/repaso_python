from tkinter import *
top = Tk()

def main():
    top['bg'] = 'light gray'
    Button(top, text="Left 1").pack(side='left')
    Button(top, text="Left 2").pack(side='left')
    Button(top, text="Right 1").pack(side='right')
    Button(top, text="Right 2").pack(side='right', padx=10)
    Button(top, text="Top 1").pack(side='top')
    Button(top, text="Top 2").pack(side='top')
    Button(top, text="Bottom 1").pack(side='bottom')
    Button(top, text="Bottom 2").pack(side='bottom', pady=10)
    mainloop()

main()