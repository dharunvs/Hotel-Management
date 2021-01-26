from tkinter import *
from settings import *


class BillApp:
    def __init__(self):
        self.root = None

        self.frame1 = Frame
        self.frame2 = Frame
        self.frame3 = Frame

    def run(self):

        # SETUP

        self.window = Tk()
        self.window.attributes("-fullscreen", True)
        # self.window.state("zoomed")
        W = self.window.winfo_screenwidth()
        H = self.window.winfo_screenheight()

        self.window.geometry("{0}x{1}".format(W, H))
        self.window.resizable(False, False)
        self.window.title("Hello World")
        self.window.configure(bg=BACKGROUND)

        # -----------------------------------

        self.frame1 = Frame(self.window, height=(2*H)//3,
                            width=2*(W)//3, relief=RIDGE, bd=3, bg=BACKGROUND)
        self.frame2 = Frame(self.window, height=H,
                            width=W//3, relief=RIDGE, bd=3, bg=BACKGROUND)
        self.frame3 = Frame(self.window, height=H//3,
                            width=2*(W)//3, relief=RIDGE, bd=3, bg=BACKGROUND)

        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1, rowspan=2)
        self.frame3.grid(row=1, column=0)

        # -----------------------------------

        self.window.mainloop()

# ------------------------------- HELPERS ------------------------------------

    def my_label(self, text, fg=TEXT):
        return Label(self.root, text=text, bg=BACKGROUND, fg=fg, font=FONT)

# ----------------------------------------------------------------------------
