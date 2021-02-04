from tkinter import *
from settings import *
from manage_data import Database

try:
    from kot_gui import *
except:
    pass


class POS:
    def __init__(self):
        self.root = None
        self.dbase = Database()
        self.kotc = KOT()

        self.frame1 = Frame
        self.frame2 = Frame
        self.frame3 = Frame

        self.bill_frame = Frame
        self.items_frame = Frame
        self.control_frame = Frame

        self.items_list = []
        for row in self.dbase.get_from_dbitems():
            self.items_list.append(row)

        self.items_button_list = []

        self.price = 0
        self.tax = 18
        self.total_price = self.price + self.price*(self.tax//100)

        self.selected_items = []

    def run(self):

        # SETUP

        self.window = Tk()
        # self.window.attributes("-fullscreen", True)
        self.W = POS_WIDTH
        self.H = POS_HEIGHT

        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws/2) - (self.W/2)
        y = (hs/2) - (self.H/2)

        self.window.geometry(f"{self.W}x{self.H}+{int(x)}+{int(y-40)}")
        self.window.resizable(False, False)
        self.window.title("POS")
        self.window.configure(bg=BACKGROUND)

        # -----------------------------------

        self.frame1 = Frame(self.window, height=(2*self.H)//3,
                            width=2*(self.W)//3, relief=RIDGE, bd=3, bg=BACKGROUND)
        self.frame2 = Frame(self.window, height=self.H,
                            width=self.W//3, relief=RIDGE, bd=3, bg=BACKGROUND)
        self.frame3 = Frame(self.window, height=self.H//3,
                            width=2*(self.W)//3, relief=RIDGE, bd=3, bg=BACKGROUND)

        self.bill_frame = Frame(self.frame1, relief=RIDGE, height=(2*self.H)//3,
                                width=2*(self.W)//3, bg=BACKGROUND)
        self.items_frame = Frame(self.frame2, relief=RIDGE, bd=10, height=self.H,
                                 width=self.W//3, bg=BACKGROUND)
        self.control_frame = Frame(self.frame3, relief=RIDGE, height=self.H//3,
                                   width=2*(self.W)//3, bg=BACKGROUND)

        self.types_frame = Frame(self.frame2, relief=RIDGE, bd=6,
                                 width=(self.W//3)-8, bg=BACKGROUND)

        cuisines = ["INDIAN", "CHINESE", "ITALIAN",
                    "ARABIC", "CHAT", "DESSERTS"]

        r = 0
        for i in range(len(cuisines)):
            self.type = Button(
                self.types_frame, text=cuisines[i], font=FONT, width=16, bg=BACKGROUND,
                fg=YELLOW, command=lambda j=cuisines[i]: self.add_items_display(j))

            c = 0
            if i % 2 == 0:
                r += 1
            else:
                c = 1
            self.type.grid(row=r, column=c, pady=12, padx=15)

        self.add_items_display("CHINESE")

        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1, rowspan=2)
        self.frame3.grid(row=1, column=0)

        self.items_frame.place(x=0, y=0)
        self.types_frame.place(x=20, y=518)
        self.bill_frame.place(x=0, y=0)
        self.control_frame.place(x=0, y=0)
        self.control_frame.grid_propagate(0)

        # -----------------------------------

        self.build_bill_frame()

        # -----------------------------------
        self.price_display = Frame(
            self.control_frame, bd=3, relief=RIDGE, width=250, height=120, bg=BACKGROUND)
        self.price_display.grid(row=0, column=2, rowspan=3, padx=100, sticky=E)

        self.order_label = Label(
            self.control_frame, text="Order No", font=FONT, bg=BACKGROUND, fg=FOREGROUND)
        self.table_label = Label(
            self.control_frame, text="Table No", font=FONT, bg=BACKGROUND, fg=FOREGROUND)
        self.name_label = Label(
            self.control_frame, text="Name", font=FONT, bg=BACKGROUND, fg=FOREGROUND)

        self.order_entry = Entry(self.control_frame, font=FONT, width=2)
        self.table_entry = Entry(self.control_frame, font=FONT, width=2)
        self.name_entry = Entry(self.control_frame, font=FONT, width=20)

        self.order_but = Button(
            self.control_frame, text="Order", width=10, font=FONT1(12), bg=BACKGROUND, fg=WHITE, command=self.order)

        self.order_but.grid(row=3, column=2)

        self.order_label.grid(row=0, column=0, padx=15, sticky=W)
        self.table_label.grid(row=1, column=0, padx=15, sticky=W)
        self.name_label.grid(row=2, column=0, padx=15, sticky=W)
        self.order_entry.grid(row=0, column=1, padx=15, sticky=W)
        self.table_entry.grid(row=1, column=1, padx=15, sticky=W)
        self.name_entry.grid(row=2, column=1, padx=15, sticky=W)

        # -----------------------------------

        self.price1_label1 = Label(
            self.price_display, text=f"Price", font=FONT1(20), bg=BACKGROUND, fg=FOREGROUND)

        self.tax_label = Label(
            self.price_display, text=f"Tax", font=FONT1(20), bg=BACKGROUND, fg=FOREGROUND)

        self.tprice_label = Label(
            self.price_display, text=f"Total", font=FONT1(20), bg=BACKGROUND, fg=FOREGROUND)

        self.tax1_label = Label(
            self.price_display, text=f"{self.tax}%", font=FONT1(16), bg=BACKGROUND, fg=FOREGROUND)

        self.price1_label1.grid(row=0, column=0, padx=15)
        self.tax_label.grid(row=1, column=0, padx=15)
        self.tprice_label.grid(row=2, column=0, padx=15)

        self.tax1_label.grid(row=1, column=1, padx=15)

        self.add_price()
        # -----------------------------------

        self.kot_but = Button(self.control_frame, text="KOT",
                              bg=BACKGROUND, fg=YELLOW, font=FONT1(20), command=self.kot)
        self.kot_but.grid(row=3, column=0)

        # -----------------------------------

        self.window.mainloop()

# ------------------------------- HELPERS ------------------------------------

    def item_onclick(self, item):
        self.selected_items.append(item)
        self.add_item_bill(item)
        # print(self.selected_items)

    def type_onclick(self, item):
        print(item)

    def add_item(self):
        name = self.item_entry.get()

        for i in self.items_list:
            if name == i[1]:
                self.selected_items.append(i)
                self.add_item_bill()

    def add_item_bill(self, item):
        self.price = 0
        for i in range(len(self.selected_items)):
            self.count = self.selected_items.count(self.selected_items[i])

            if self.count <= 1:
                self.label1 = Label(self.items_miniframe,
                                    text=f"{self.selected_items[i][0]}", bg=BACKGROUND, fg=FOREGROUND, font=FONT)
                self.label2 = Label(self.items_miniframe,
                                    text=f"{self.selected_items[i][1]}", bg=BACKGROUND, fg=FOREGROUND, font=FONT)
                self.label3 = Label(self.items_miniframe,
                                    text=f"{self.selected_items[i][2]}", bg=BACKGROUND, fg=FOREGROUND, font=FONT)
                self.label4 = Label(self.items_miniframe, text=f"{self.count}",
                                    bg=BACKGROUND, fg=FOREGROUND, font=FONT)
                self.button5 = Button(self.items_miniframe, text="x", bg=BACKGROUND, fg=YELLOW, width=2, height=1,  font=FONT1(
                    12), command=lambda j=self.selected_items[i]: self.remove(j))
                self.button5.grid_propagate(0)

                self.label6 = Label(self.items_miniframe, text=f"{self.count*self.selected_items[i][2]}",
                                    bg=BACKGROUND, fg=FOREGROUND, font=FONT)

                self.label1.grid(row=i+2, column=0, padx=20)
                self.label2.grid(row=i+2, column=1, padx=20)
                self.label3.grid(row=i+2, column=2, padx=20)
                self.label4.grid(row=i+2, column=3, padx=20)
                self.button5.grid(row=i+2, column=4, padx=20)
                self.label6.grid(row=i+2, column=5, padx=20)

            else:
                self.label4["text"] = self.count
                self.label6["text"] = self.count*self.selected_items[i][2]

        self.items_miniframe.update()
        for i in self.selected_items:
            self.price += i[2]

        self.total_price = self.price + self.price*(self.tax/100)
        self.add_price()

    def build_bill_frame(self):
        try:
            self.items_miniframe.destroy()
        except:
            pass

        self.item_entry = Entry(self.bill_frame, font=FONT, width=20)

        self.item_entry.place(x=10, y=10)
        self.add_but = Button(self.bill_frame, font=FONT,
                              text="Add item", command=self.add_item)
        self.add_but.place(x=300, y=10)

        self.items_miniframe = Frame(self.bill_frame, relief=RIDGE, bg=BACKGROUND, height=(2*self.H)//3 - 150,
                                     width=2*(self.W)//3 - 50)
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
        self.name_label.grid(row=0, column=1, padx=10)
        self.price_label = Label(self.items_miniframe, text="PRICE",
                                 font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=2, padx=20)
        self.quantity_label = Label(self.items_miniframe, text="QUANTITY",
                                    font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=3, padx=20)
        self.remove_label = Label(self.items_miniframe, text="REMOVE",
                                  font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=4, padx=20)
        self.final_label = Label(self.items_miniframe, text="FINAL",
                                 font=FONT, bg=BACKGROUND, fg=YELLOW).grid(row=0, column=5, padx=20)

        # self.mini_mini_frame = Frame(
        #     self.items_miniframe, bg=BACKGROUND, width=800, height=500, relief=RIDGE)
        # self.mini_mini_frame.grid(row=1, column=0, columnspan=8)

    def add_price(self):
        try:
            self.price1_label.destroy()
            self.tprice1_label.destroy()
        except:
            pass

        self.price1_label = Label(
            self.price_display, text=f"{self.price}", font=FONT1(16), bg=BACKGROUND, fg=YELLOW)
        self.tprice1_label = Label(
            self.price_display, text=f"{self.total_price}", font=FONT1(16), bg=BACKGROUND, fg=YELLOW)

        self.price1_label.grid(row=0, column=1, padx=15)
        self.tprice1_label.grid(row=2, column=1, padx=15)

    def order(self):
        items_raw = self.selected_items
        final_list = ""

        for i in set(items_raw):
            final_list += f'''"{i[1]}-{items_raw.count(i)}"'''

        table = self.table_entry.get()
        order = self.order_entry.get()
        name = self.name_entry.get()

        data = f'''{order}, {table}, {final_list}, "{name}"'''

        self.dbase.add_to_dbkot(data)
        self.selected_items = []
        self.price = 0
        self.total_price = 0
        self.order_entry.delete(0, END)
        self.table_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.build_bill_frame()
        self.add_price()

    def print1(self):
        pass

    def add_items_display(self, item):
        try:
            for i in self.items_frame.winfo_children():
                i.destroy()
        except:
            pass

        r = 0
        for i in range(len(self.items_list)):
            if self.items_list[i][3] == item:
                self.a = Button(self.items_frame,
                                text=self.items_list[i][1], font=FONT, width=16, bg=BACKGROUND,
                                fg=FOREGROUND, command=lambda j=self.items_list[i]: self.item_onclick(j))

                c = 0
                if i % 2 == 0:
                    r += 1
                else:
                    c = 1
                self.a.grid(row=r, column=c, pady=5, padx=5)
                self.items_button_list.append(self.a)

# ----------------------------------------------------------------------------

    def kot(self):
        try:
            self.kotc.run()
            self.window.destroy()
        except:
            pass

    def remove(self, item):
        self.selected_items.remove(item)
        self.count -= 1
        self.label4["text"] = f"{self.count}"
        self.label6["text"] = self.count*item[2]

        if self.count == 0:
            self.label1.destroy()
            self.label2.destroy()
            self.label3.destroy()
            self.label4.destroy()
            self.button5.destroy()

            self.label6.destroy()
