from tkinter import *
from settings import *
from admin_gui import *
from pos_gui import *
from kot_gui import *


class App:
    def __init__(self):
        self.root = None
        self.adminC = AdminApp()
        self.posC = BillApp()
        self.kotc = KOT()

        self.admin_but = Button
        self.pos_but = Button
        self.lot_but = Button

        self.f1 = Frame
        self.f2 = Frame
        self.f3 = Frame

    def run(self):

        # SETUP

        self.window = Tk()
        W = MAIN_WIDTH
        H = MAIN_HEIGHT
        # self.window.geometry(f"{W}x{H}")
        self.window.resizable(False, False)
        self.window.title("Hello World")
        self.window.configure(bg=BACKGROUND)

        # -----------------------------------

        self.f1 = Frame(self.window, bg=BACKGROUND, height=H, width=W //
                        3).grid(row=0, column=0)
        self.f2 = Frame(self.window, bg=BACKGROUND, height=H, width=W //
                        3).grid(row=0, column=1)
        self.f3 = Frame(self.window, bg=BACKGROUND, height=H, width=W //
                        3).grid(row=0, column=2)

        self.admin_but = Button(self.f1, text="ADMIN", fg=FOREGROUND, bg=BACKGROUND, bd=5,
                                font=FONT1(48), activebackground=FOREGROUND, width=6, command=self.admin)
        self.pos_but = Button(self.f1, text="POS", fg=FOREGROUND, bg=BACKGROUND, bd=5,
                              font=FONT1(48), activebackground=FOREGROUND, width=6, command=self.pos)
        self.kot_but = Button(self.f1, text="KOT", fg=FOREGROUND, bg=BACKGROUND, bd=5,
                              font=FONT1(48), activebackground=FOREGROUND, width=6, command=self.kot)

        self.admin_but.grid(row=0, column=0)
        self.pos_but.grid(row=0, column=1)
        self.kot_but.grid(row=0, column=2)

        # -----------------------------------

        self.window.mainloop()

# ------------------------------- HELPERS ------------------------------------

    def my_label(self, text, fg=TEXT):
        return Label(self.root, text=text, bg=BACKGROUND, fg=fg, font=FONT)

    def admin(self):
        self.window.destroy()
        self.adminC.password_window()

    def pos(self):
        self.window.destroy()
        self.posC.run()

    def kot(self):
        self.window.destroy()
        self.kotc.run()


# ----------------------------------------------------------------------------
