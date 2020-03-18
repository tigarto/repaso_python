import tkinter as tk

# Declare global variables
counter = None

# This function is called whenever the button is pressed
def count():

    global counter

    # Increment counter by 1
    counter.set(counter.get() + 1)

# Create the main window
root = tk.Tk()
root.title("Counter")

# Tkinter variable for holding a counter
counter = tk.IntVar()
counter.set(0)

# Create widgets (note that command is set to count and not count() )
label_counter = tk.Label(root, width=7, textvariable=counter)
button_counter = tk.Button(root, text="Count", command=count)

# Lay out widgets
label_counter.pack()
button_counter.pack()

# Run forever!
root.mainloop()

