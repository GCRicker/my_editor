import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    pass

def change_font():
    pass

def new_file():
    pass

def open_file():
    pass

def save_file():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def about():
    pass

def quit():
    pass


window = Tk()
window.title("Text Editor Program")
file = None

window_width = 500
window_height = 500

# find the Screen Center
screen_width = window.winfo_screenwidth()       # The total screen width in pixels
screen_height = window.winfo_screenheight()     # The total screen height in pixels
x = int((screen_width/2) - (window_width/2))    # Have the windows center in the screen's center
y = int((screen_height/2) - (window_height/2))  # Have the windows center in the screen's center
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))



window.mainloop()
