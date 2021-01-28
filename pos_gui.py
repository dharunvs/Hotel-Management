from tkinter import *
from settings import *
from manage_data import Database


class BillApp:
    def __init__(self):
        self.root = None
        self.dbase = Database()

        self.frame1 = Frame
        self.frame2 = Frame
        self.frame3 = Frame

        self.bill_frame = Frame
        self.items_frame = Frame
        self.control_frame = Frame

        self.items_list = []
        for row in self.dbase.get_from_db():
            self.items_list.append(row)

        self.items_button_list = []

        self.selected_items = []

    def run(self):

        # SETUP

        self.window = Tk()
        self.window.attributes("-fullscreen", True)
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

        self.bill_frame = Frame(self.frame1, relief=RIDGE, bd=10, width=20)
        self.items_frame = Frame(self.frame2, relief=RIDGE, bd=10, width=20)
        self.control_frame = Frame(self.frame3, relief=RIDGE, bd=10, width=20)

        for i in self.items_list:
            self.a = Button(self.items_frame,
                            text=i[1], command=lambda j=i: self.item_onclick(j))
            self.a.pack()
            self.items_button_list.append(self.a)

        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1, rowspan=2)
        self.frame3.grid(row=1, column=0)

        self.items_frame.place(x=0, y=0)
        self.bill_frame.place(x=0, y=0)
        self.control_frame.place(x=0, y=0)

        # -----------------------------------

        # -----------------------------------

        # -----------------------------------

        self.window.mainloop()

# ------------------------------- HELPERS ------------------------------------

    def my_label(self, text, fg=TEXT):
        return Label(self.root, text=text, bg=BACKGROUND, fg=fg, font=FONT)

    def item_onclick(self, j):
        self.selected_items.append(j)
        self.add_item(j)
        print(j)

    def add_item(self, item):
        code = item[0]
        name = item[1]
        price = item[2]

        self.frame20 = Frame(self.bill_frame, bd=3,
                             relief=RIDGE, height=50, width=600)
        self.frame20.configure(
            height=self.frame20["height"], width=self.frame20["width"])
        self.frame20.grid_propagate(0)
        self.frame20.pack()

        self.add_item_2()

    def add_item_2(self):

        code_frame = Frame(self.frame20, height=20,
                           width=20, bd=3, relief=RIDGE)
        code_frame.configure(
            height=self.frame20["height"], width=self.frame20["width"])
        code_frame.grid_propagate(0)
        code_frame.place(x=0, y=0)

        name_frame = Frame(self.frame20, height=40,
                           width=50, bd=3, relief=RIDGE)
        price_frame = Frame(self.frame20, height=40,
                            width=50, bd=3, relief=RIDGE)


# ----------------------------------------------------------------------------
