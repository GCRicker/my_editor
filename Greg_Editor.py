# pylint: disable=unused-wildcard-import, method-hidden
# pylint: enable=too-many-lines

import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="Please pick a color")
    text_area.config(
        fg=color[1]
    )  # color chooses returns a tuple, let's just used the hex value


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


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
screen_width = window.winfo_screenwidth()  # The total screen width in pixels
screen_height = window.winfo_screenheight()  # The total screen height in pixels
x = int(
    (screen_width / 2) - (window_width / 2)
)  # Have the windows center in the screen's center
y = int(
    (screen_height / 2) - (window_height / 2)
)  # Have the windows center in the screen's center
window.geometry(
    "{}x{}+{}+{}".format(window_width, window_height, x, y)
)  # size,size, position, position

font_name = StringVar(window)  # not sure why window is being passed
font_name.set("Arial")

font_size = StringVar(window)  # not sure why window is being passed
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)  # Used for word wrap and resize window I think
window.grid_columnconfigure(0, weight=1)  # Used for word wrap and resize window I think
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(
    frame, font_name, *font.families(), command=change_font
)  # *font.families()  shows fonts
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)


scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)


window.mainloop()
