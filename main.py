# imports
import requests
import stdiomask
from tkinter import *

# Initializes window object
window = Tk()
label = Label(window, text="Hello", font=("Arial Bold", 50))
label.grid(column=0, row=0)
btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)
# This renders the window
window.mainloop()
