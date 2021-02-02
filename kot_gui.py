from tkinter import *
from settings import *
from manage_data import Database


class KOT:
    def __init__(self):
        self.window = None
        self.dbase = Database()

        W = KOT_WIDTH
        H = KOT_HEIGHT

        self.main_list = self.dbase.get_from_dbkot()

        self.main_frame = Frame
        self.side_frame = Frame

    def run(self):
        self.window = Tk()
        # self.window.attributes("-fullscreen", True)
        W = KOT_WIDTH
        H = KOT_HEIGHT

        self.window.geometry(f"{W}x{H}")
        self.window.resizable(False, False)
        self.window.title("KOT")
        self.window.configure(bg=BACKGROUND)

        # ---------------------------------------------------

        self.main_frame = Frame(
            self.window, bd=3, relief=RIDGE, bg=BACKGROUND, width=W, height=(3*H)//4)
        self.side_frame = Frame(
            self.window, bd=3, relief=RIDGE, bg=BACKGROUND, width=W, height=(1*H)//4)

        self.main_frame.grid_propagate(0)
        self.main_frame.grid(row=0, column=0)

        self.side_frame.grid_propagate(0)
        self.side_frame.grid(row=1, column=0)

        self.data()

        # ---------------------------------------------------

        # ---------------------------------------------------

        self.window.mainloop()

    def data(self):

        r = 0
        c = 0

        for i in range(len(self.main_list)):
            order = self.main_list[i][0]
            table = self.main_list[i][1]
            items = self.main_list[i][2]

            items = items.split("\"")
            new_items = []
            for k in items:
                new_items.append(tuple(k.split("-")))

            frame = Frame(self.main_frame, width=100, height=200,
                          bd=3, relief=RIDGE, bg=BACKGROUND)
            order_label = Label(
                frame, text="Order No", font=FONT, bg=BACKGROUND, fg=FOREGROUND).grid(row=0, column=0)
            ordern_label = Label(
                frame, text=f"{order}", font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=1)
            table_label = Label(
                frame, text="Table No", font=FONT, bg=BACKGROUND, fg=FOREGROUND).grid(row=1, column=0, pady=10)
            tablen_label = Label(
                frame, text=f"{table}", font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=1, column=1, pady=10)

            item_frame = Frame(frame, width=1280/6, height=200,
                               bd=3, relief=RIDGE, bg=BACKGROUND)
            item_frame.grid_propagate(0)
            for j in new_items:
                items_label = Label(
                    item_frame, text=f"{j[0]} - {j[1]}", font=FONT1(12), bg=BACKGROUND, fg=YELLOW)
                items_label.grid(sticky=E, padx=10)

            item_frame.grid(row=2, column=0, columnspan=2)

            done_button = Button(frame, text="Done", font=FONT,
                                 bg=BACKGROUND, fg=YELLOW, command=lambda j=self.main_list[i]: self.done(j[0]))
            done_button.grid(columnspan=2, pady=10)

            if i % 6 == 0:
                r += 1

            else:
                c += 1
            frame.grid(row=r, column=c)


# ------------------------------- HELPERS ------------------------------------


    def done(self, order):
        a = self.main_frame.winfo_children()
        for i in range(len(a)):
            b = a[i].winfo_children()
            for j in range(len(b)):
                if b[1]["text"] == str(order):
                    a[i].destroy()
