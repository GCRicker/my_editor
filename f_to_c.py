from tkinter import *


def convert():
    F = float(fahrenheit_entry.get())
    C = (F - 32) * 5 / 9
    display_celsius_label["text"] = str(C)


my_window = Tk()

# create labels
friendly_label_1 = Label(my_window, text="Enter Fahrenheit")
friendly_label_2 = Label(my_window, text="Celsius Temperature")
display_celsius_label = Label(my_window)

# create remaining widgets
fahrenheit_entry = Entry(my_window)
convert_button = Button(my_window, text="Convert", command=convert)

# add everything nicely into the window
friendly_label_1.grid(row=0, column=0)
fahrenheit_entry.grid(row=0, column=1)
friendly_label_2.grid(row=1, column=0)
display_celsius_label.grid(row=1, column=1)
convert_button.grid(row=2, column=0)

my_window.mainloop()
