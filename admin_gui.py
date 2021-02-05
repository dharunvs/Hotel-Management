from tkinter import *
from tkinter import ttk
from settings import *
from manage_data import Database


class Admin:
    def __init__(self):
        self.root = None
        self.dbase = Database()
        self.code_entry = Entry
        self.name_entry = Entry
        self.price_entry = Entry
        self.add_button = Button
        self.password_entry = Entry

    def run(self):

        # SETUP
        # self.root = Tk()
        # self.root.attributes("-fullscreen", True)
        # # self.root.state("zoomed")
        # W = self.root.winfo_screenwidth()
        # H = self.root.winfo_screenheight()

        # self.root.geometry("{0}x{1}".format(W, H))
        # self.root.resizable(False, False)
        # self.root.title("Hello World")
        # self.root.configure(bg=BACKGROUND)

        self.root = Tk()
        self.W = POS_WIDTH
        self.H = POS_HEIGHT

        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (self.W/2)
        y = (hs/2) - (self.H/2)

        self.root.geometry(f"{self.W}x{self.H}+{int(x)}+{int(y-40)}")
        # self.root.geometry(f"{DATA_WIDTH}x{DATA_HEIGHT}")
        self.root.resizable(False, False)
        self.root.title("Admin")
        self.root.configure(bg=BACKGROUND)

        # -----------------------------------

        self.code_entry = Entry(self.root, font=FONT, width=10)
        self.name_entry = Entry(self.root, font=FONT, width=30)
        self.price_entry = Entry(self.root, font=FONT, width=10)

        n = StringVar()
        self.type_entry = ttk.Combobox(
            self.root, width=20, font=FONT, textvariable=n)
        self.type_entry["values"] = (
            "INDIAN", "CHINESE", "ITALIAN", "ARABIC", "CHAT", "DESSERTS")

        self.code_label = Label(self.root, text="CODE",
                                font=FONT, bg=BACKGROUND, fg=FOREGROUND)
        self.name_label = Label(self.root, text="NAME",
                                font=FONT, bg=BACKGROUND, fg=FOREGROUND)
        self.price_label = Label(
            self.root, text="PRICE", font=FONT, bg=BACKGROUND, fg=FOREGROUND)
        self.type_label = Label(
            self.root, text="TYPE", font=FONT, bg=BACKGROUND, fg=FOREGROUND)

        self.add_button = Button(
            self.root, text="Add", width=6, font=FONT, borderwidth=0, bg=FOREGROUND, fg=TEXT, command=self.add_data)
        self.delete_button = Button(
            self.root, text="Delete", width=6, font=FONT, borderwidth=0, bg=FOREGROUND, fg=TEXT, command=self.delete_data)

        self.tree_frame = Frame(self.root, width=1260, height=640)
        self.tree_frame.pack_propagate(0)

        self.main_tree()

        # -----------------------------------

        self.root.mainloop()

# ------------------------------- HELPERS ------------------------------------

    def get_data(self):
        code = self.code_entry.get()
        name = self.name_entry.get()
        price = self.price_entry.get()
        type = self.type_entry.get()

        self.item_string = f'''{code}, "{name}", {price}, "{type}"'''

        self.code_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.type_entry.delete(0, END)

        return self.item_string

    def add_data(self):
        item = self.get_data()
        self.dbase.add_to_dbitems(item)
        self.show()

    def show(self):
        info = self.dbase.get_from_dbitems()
        if self.item_string != ", , ":
            self.sheet.insert("", END, values=info[len(info)-1])

    def delete_data(self):
        name = self.name_entry.get()
        code = self.code_entry.get()

        if name != "":
            try:
                self.dbase.delete_from_dbitems_uname(name)
            except:
                pass

        if code != "":
            try:
                self.dbase.delete_from_dbitems_ucode(code)
            except:
                pass

        self.code_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.type_entry.delete(0, END)

        self.main_tree()

    def password_window(self):
        self.win = Tk()
        # self.win.attributes("-fullscreen", True)
        self.win.configure(bg=BACKGROUND)
        self.win.resizable(False, False)

        frame = Frame(self.win, height=200, width=400, bg=BACKGROUND)
        frame.pack(fill=BOTH, expand=True)

        password_label = Label(frame, text="Enter Password", font=FONT1(20),
                               bg=BACKGROUND, fg=FOREGROUND).grid(row=0, column=0, padx=10, sticky=W, pady=10)
        self.password_entry = Entry(frame, show="*", font=FONT, width=30)
        submit = Button(frame, text="Submit", font=FONT1(20), bd=5, bg=BACKGROUND, fg=FOREGROUND, command=self.password_check).grid(
            row=2, column=0, sticky=E, padx=10, pady=10)

        self.password_entry.grid(row=1, column=0, sticky=W, padx=10, pady=10)
        self.win.mainloop()

    def password_check(self):
        password = self.password_entry.get()
        if password == PASSWORD:
            self.win.destroy()
            self.run()
        else:
            self.password_entry.delete(0, END)

    def main_tree(self):
        try:
            self.sheet.destroy()
            self.vsb.destroy()
        except:
            pass

        self.sheet = ttk.Treeview(self.tree_frame, column=(
            "CODE", "NAME", "PRICE", "TYPE"), show="headings")

        self.vsb = ttk.Scrollbar(self.tree_frame, orient="vertical",
                                 command=self.sheet.yview)
        self.vsb.pack(side=RIGHT, fill=Y)

        self.sheet.configure(yscrollcommand=self.vsb.set)

        style = ttk.Style()
        style.configure("Treeview", font=FONT, rowheight=30,
                        bg=BACKGROUND, fg=FOREGROUND)
        style.configure("Treeview.Heading", font=FONT1(20), rowheight=40,
                        bg=BACKGROUND, fg=FOREGROUND)

        for row in self.dbase.get_from_dbitems():
            self.sheet.insert("", END, values=row)

        self.sheet.column("#1", anchor=CENTER, stretch=YES)
        self.sheet.heading("#1", text="CODE")
        self.sheet.column("#2", anchor=CENTER, stretch=YES)
        self.sheet.heading("#2", text="NAME")
        self.sheet.column("#3", anchor=CENTER, stretch=YES)
        self.sheet.heading("#3", text="PRICE")
        self.sheet.column("#4", anchor=CENTER, stretch=YES)
        self.sheet.heading("#4", text="TYPE")

        self.code_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_label.grid(row=0, column=1, padx=5, pady=5)
        self.price_label.grid(row=0, column=2, padx=5, pady=5)
        self.type_label.grid(row=0, column=3, padx=5, pady=5)

        self.code_entry.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.price_entry.grid(row=1, column=2, padx=5, pady=5)
        self.type_entry.grid(row=1, column=3, padx=5, pady=5)
        self.type_entry.current()

        self.add_button.grid(row=1, column=4, padx=5, pady=5)
        self.delete_button.grid(row=1, column=5, padx=5, pady=5)

        self.tree_frame.grid(row=4, column=0, columnspan=6,
                             padx=5, pady=5)
        self.sheet.pack(fill=BOTH, side=LEFT, expand=1)


# ----------------------------------------------------------------------------
