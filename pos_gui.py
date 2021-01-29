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
        # self.window.attributes("-fullscreen", True)
        W = POS_WIDTH
        H = POS_HEIGHT

        # self.window.geometry("{0}x{1}".format(W, H))

        self.window.geometry(f"{W}x{H}")
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

        self.bill_frame = Frame(self.frame1, relief=RIDGE, bd=10, height=(2*H)//3,
                                width=2*(W)//3, bg=BACKGROUND)
        self.items_frame = Frame(self.frame2, relief=RIDGE, bd=10, height=H,
                                 width=W//3, bg=BACKGROUND)
        self.control_frame = Frame(self.frame3, relief=RIDGE, bd=10, height=H//3,
                                   width=2*(W)//3, bg=BACKGROUND)

        for i in self.items_list:
            self.a = Button(self.items_frame,
                            text=i[1], command=lambda j=i: self.item_onclick(j))

            # , command=lambda j=i: self.item_onclick(j)

            self.a.pack()
            self.items_button_list.append(self.a)

        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1, rowspan=2)
        self.frame3.grid(row=1, column=0)

        self.items_frame.place(x=0, y=0)
        self.bill_frame.place(x=0, y=0)
        self.control_frame.place(x=0, y=0)

        # -----------------------------------

        self.item_entry = Entry(self.bill_frame, font=FONT, width=20)

        self.item_entry.place(x=10, y=10)
        self.add_but = Button(self.bill_frame, font=FONT,
                              text="Add item", command=self.add_item)
        self.add_but.place(x=300, y=10)

        self.items_miniframe = Frame(self.bill_frame, relief=RIDGE, bg=BACKGROUND, height=(2*H)//3 - 150,
                                     width=2*(W)//3 - 50)
        self.items_miniframe.place(x=10, y=100)

        # v = Scrollbar(self.items_miniframe, orient='horizontal')
        # v.config(command=self.items_miniframe.yview)
        # v.pack(side=RIGHT, fill=Y)

        # self.items_miniframe.configure(
        #     height=self.items_miniframe["height"], width=self.items_miniframe["width"])
        self.items_miniframe.grid_propagate(0)

        self.code_label = Label(self.items_miniframe, text="CODE",
                                font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=0, padx=20)
        self.name_label = Label(self.items_miniframe, text="NAME",
                                font=FONT, bg=BACKGROUND, fg=YELLOW)
        self.name_label.grid(row=0, column=1, padx=10, columnspan=2)
        self.price_label = Label(self.items_miniframe, text="PRICE",
                                 font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=3, padx=20)
        self.quantity_label = Label(self.items_miniframe, text="QUANTITY",
                                    font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=4, padx=20)
        self.add_label = Label(self.items_miniframe, text="ADD",
                               font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=5, padx=20)
        self.remove_label = Label(self.items_miniframe, text="REMOVE",
                                  font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=6, padx=20)
        self.final_label = Label(self.items_miniframe, text="FINAL",
                                 font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=7, padx=20)

        # self.minimini_frame = Frame(
        #     self.items_miniframe, bg=BACKGROUND, width=800, height=500, relief=RIDGE)
        # self.minimini_frame.grid(row=1, column=0, columnspan=8)
        # -----------------------------------

        # -----------------------------------

        self.window.mainloop()

# ------------------------------- HELPERS ------------------------------------

    def item_onclick(self, item):
        self.selected_items.append(item)
        # self.add_item(item)
        self.add_item_bill()
        print(item)

    def add_item(self):
        name = self.item_entry.get()

        for i in self.items_list:
            if name == i[1]:
                self.selected_items.append(i)
                self.add_item_bill()

    def add_item_bill(self):
        for i in range(len(self.selected_items)):
            label1 = Label(self.items_miniframe,
                           text=f"{self.selected_items[i][0]}", bg=BACKGROUND, fg=FOREGROUND, font=FONT)
            label2 = Label(self.items_miniframe,
                           text=f"{self.selected_items[i][1]}", bg=BACKGROUND, fg=FOREGROUND, font=FONT)
            label3 = Label(self.items_miniframe,
                           text=f"{self.selected_items[i][2]}", bg=BACKGROUND, fg=FOREGROUND, font=FONT)

            label4 = Label(self.items_miniframe, text="1",
                           bg=BACKGROUND, fg=BACKGROUND, font=FONT)

            label1.grid(row=i+2, column=0, padx=20)
            label2.grid(row=i+2, column=1, columnspan=2, padx=20)
            label3.grid(row=i+2, column=3, padx=20)
            label4.grid(row=i+2, column=4, padx=20)

# ----------------------------------------------------------------------------
