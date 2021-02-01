# import sqlite3

# con = sqlite3.connect("data/data.db")
# cur = con.cursor()

# cur.execute(
#     '''CREATE TABLE KOT(
#         ORDER_NO int,
#         TABLE_NO int,
#         ITEMS varchar(255)
#     );''')

# result = cur.fetchall()
# print(result)

# import tkinter as tk

# import tksheet

# top = tk.Tk()

# sheet = tksheet.Sheet(top)

# sheet.place(x=10, y=10)

# sheet.set_sheet_data([[f"{ri+cj}" for cj in range(3)] for ri in range(1)])

# # table enable choices listed below:

# sheet.enable_bindings(("single_select",

#                        "row_select",

#                        "column_width_resize",

#                        "arrowkeys",

#                        "right_click_popup_menu",

#                        "rc_select",

#                        "rc_insert_row",

#                        "rc_delete_row",

#                        "copy",

#                        "cut",

#                        "paste",

#                        "delete",

#                        "undo",

#                        "edit_cell"))

# top.mainloop()

# from tkinter import ttk
# import tkinter as tk
# import sqlite3


# def connect():
#     con1 = sqlite3.connect("data/data.db")
#     cur1 = con1.cursor()
#     con1.commit()
#     con1.close()


# def View():
#     con1 = sqlite3.connect("data/data.db")
#     cur1 = con1.cursor()
#     cur1.execute("SELECT * FROM ITEMS")
#     rows = cur1.fetchall()

#     for row in rows:
#         print(row)
#         tree.insert("", tk.END, values=row)

#     con1.close()


# connect()
# root = tk.Tk()

# tree = ttk.Treeview(root, column=("CODE", "NAME", "PRICE"), show='headings')

# tree.column("#1", anchor=tk.CENTER)
# tree.heading("#1", text="CODE")
# tree.column("#2", anchor=tk.CENTER)
# tree.heading("#2", text="NAME")
# tree.column("#3", anchor=tk.CENTER)
# tree.heading("#3", text="PRICE")
# tree.pack()

# button1 = tk.Button(text="Display data", command=View)
# button1.pack(pady=10)

# root.mainloop()

result = [[1, 2, "[['CHICKEN NOODLES', 1], ['BRIYANI', 2]]"],
          [22, 33, "[['NOODLES', 1], ['BRIYANI', 2]]"]]

data = ""
for i in result:
    order = i[0]
    table = i[1]
    items = eval(i[2])

    items1 = ""

    for i in items:
        items1 += f"{i[0]} {i[1]}\n\t"

    data += f'''
     Order no = {order}
     Table no = {table}
     Items = {items1}
     '''

    print(data)

    data = ""
