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
        W = POS_WIDTH
        H = POS_HEIGHT

        self.window.geometry(f"{W}x{H}")
        self.window.resizable(False, False)
        self.window.title("POS")
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

        r = 0
        for i in range(len(self.items_list)):
            self.a = Button(self.items_frame,
                            text=self.items_list[i][1], font=FONT, width=16, command=lambda j=self.items_list[i]: self.item_onclick(j))

            # , command=lambda j=i: self.item_onclick(j)

            c = 0
            if i % 2 == 0:
                r += 1
            else:
                c = 1
            self.a.grid(row=r, column=c)
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
        # -----------------------------------
        self.price_display = Frame(
            self.control_frame, bd=3, relief=RIDGE, width=250, height=120, bg=BACKGROUND)
        self.price_display.place(x=600, y=20)

        self.order_label = Label(
            self.control_frame, text="Order No", font=FONT, bg=BACKGROUND, fg=FOREGROUND)
        self.table_label = Label(
            self.control_frame, text="Table No", font=FONT, bg=BACKGROUND, fg=FOREGROUND)

        self.order_entry = Entry(self.control_frame, font=FONT, width=2)
        self.table_entry = Entry(self.control_frame, font=FONT, width=2)

        self.order_but = Button(
            self.control_frame, text="Order", width=10, font=FONT1(10), bg=BACKGROUND, fg=WHITE, command=self.order)
        self.print_but = Button(
            self.control_frame, text="Print", width=10, font=FONT1(10), bg=BACKGROUND, fg=WHITE, command=self.print1)

        self.order_but.place(x=605, y=160)
        self.print_but.place(x=700, y=160)

        self.order_label.place(x=10, y=10)
        self.table_label.place(x=10, y=60)
        self.order_entry.place(x=110, y=10)
        self.table_entry.place(x=110, y=60)

        #####################

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

        self.window.mainloop()

# ------------------------------- HELPERS ------------------------------------

    def item_onclick(self, item):
        self.selected_items.append(item)
        self.add_item_bill()
        # print(self.selected_items)

    def add_item(self):
        name = self.item_entry.get()

        for i in self.items_list:
            if name == i[1]:
                self.selected_items.append(i)
                self.add_item_bill()

    def add_item_bill(self):
        self.price = 0
        for i in range(len(self.selected_items)):
            count = self.selected_items.count(self.selected_items[i])

            label1 = Label(self.items_miniframe,
                           text=f"{self.selected_items[i][0]}", bg=BACKGROUND, fg=FOREGROUND, font=FONT)
            label2 = Label(self.items_miniframe,
                           text=f"{self.selected_items[i][1]}", bg=BACKGROUND, fg=FOREGROUND, font=FONT)
            label3 = Label(self.items_miniframe,
                           text=f"{self.selected_items[i][2]}", bg=BACKGROUND, fg=FOREGROUND, font=FONT)
            label4 = Label(self.items_miniframe, text=f"{count}",
                           bg=BACKGROUND, fg=FOREGROUND, font=FONT)

            button5 = Button(self.items_miniframe, text="x",
                             bg=BACKGROUND, fg=YELLOW, width=2, height=1,  font=FONT1(12), command=None)
            button5.grid_propagate(0)

            label1.grid(row=i+2, column=0, padx=20)
            label2.grid(row=i+2, column=1, padx=20)
            label3.grid(row=i+2, column=2, padx=20)
            label4.grid(row=i+2, column=3, padx=20)
            button5.grid(row=i+2, column=4)

            if count > 1:
                label1.destroy()
                label2.destroy()
                label3.destroy()
                # label4.destroy()
                button5.destroy()

        for i in self.selected_items:
            self.price += i[2]

        self.total_price = self.price + self.price*(self.tax/100)
        self.add_price()

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

        data = f'''{order}, {table}, {final_list}'''

        self.dbase.add_to_dbkot(data)

    def print1(self):
        pass

# ----------------------------------------------------------------------------
