# pylint: disable=unused-wildcard-import, method-hidden
# pylint: enable=too-many-lines

from tkinter import *


class DrawLineApp:
    def __init__(
        self,
        the_window,
    ):
        self.my_canvas = Canvas(the_window, width=400, height=400, bg="white")
        self.my_canvas.bind("<Button-1>", self.draw_line)
        self.my_canvas.pack()

        # Attributes
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.click_number = 0

    # Methods
    def draw_line(self, event):
        if self.click_number == 0:
            self.x1 = event.x
            self.y1 = event.y
            self.click_number = 1
        else:
            self.x2 = event.x
            self.y2 = event.y
            self.my_canvas.create_line(
                self.x1, self.y1, self.x2, self.y2, fill="black", width=10
            )
            self.click_number = 0


my_window = Tk()
my_draw_line = DrawLineApp(my_window)

my_window.mainloop()
