import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("data/data.db")
        self.cursor = self.connection.cursor()
        self.table = ""

    def add_to_dbitems(self, data):
        try:
            self.execute(
                f'''INSERT INTO ITEMS (CODE, NAME, PRICE) VALUES ({data})''')
            self.connection.commit()
        except:
            pass

    def add_to_dbkot(self, data):
        self.execute(
            f'''INSERT INTO KOT (ORDER_NO, TABLE_NO, ITEMS, NAME) VALUES ({data})''')
        self.connection.commit()

    def delete_from_dbkot(self, data):
        try:
            self.execute(
                f'''DELETE FROM KOT WHERE ORDER_NO={data}'''
            )
            self.connection.commit()
        except:
            pass

    def delete_from_dbitems_uname(self, data):
        try:
            self.execute(
                f'''DELETE FROM ITEMS WHERE NAME={data}'''
            )
            self.connection.commit()
        except:
            pass

    def delete_from_dbitems_ucode(self, data):
        try:
            self.execute(
                f'''DELETE FROM ITEMS WHERE CODE={data}'''
            )
            self.connection.commit()
        except:
            pass

    def get_from_dbitems(self):
        self.cursor.execute(f'''SELECT * FROM ITEMS''')
        info = self.cursor.fetchall()

        return info

    def get_from_dbkot(self):
        self.cursor.execute(f'''SELECT * FROM KOT''')
        info = self.cursor.fetchall()

        return info

    def close(self):
        self.connection.commit()
        self.connection.close()

# ---------------------- HELPERS -----------------------

    def execute(self, command):
        self.connection.execute(command)
