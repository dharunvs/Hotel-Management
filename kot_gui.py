from tkinter import *
from settings import *
from manage_data import Database


class KOT:
    def __init__(self):
        self.window = None

    def run(self):
        self.window = Tk()
        # self.window.attributes("-fullscreen", True)
        W = KOT_WIDTH
        H = KOT_HEIGHT

        self.window.geometry(f"{W}x{H}")
        self.window.resizable(False, False)
        self.window.title("KOT")
        self.window.configure(bg=BACKGROUND)

        self.window.mainloop()
