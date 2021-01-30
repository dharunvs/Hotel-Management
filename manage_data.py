import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("data/data.db")
        self.cursor = self.connection.cursor()
        self.table = ""

    def add_to_db(self, data):
        try:
            self.execute(
                f'''INSERT INTO ITEMS (CODE, NAME, PRICE) VALUES ({data})''')
            self.connection.commit()
        except:
            pass

    def delete_from_db_uname(self, data):
        try:
            self.execute(
                f'''DELETE FROM ITEMS WHERE NAME={data}'''
            )
            self.connection.commit()
        except:
            pass

    def delete_from_db_ucode(self, data):
        try:
            self.execute(
                f'''DELETE FROM ITEMS WHERE CODE={data}'''
            )
            self.connection.commit()
        except:
            pass

    def get_from_db(self):
        self.cursor.execute(f'''SELECT * FROM ITEMS''')
        info = self.cursor.fetchall()

        return info

    def close(self):
        self.connection.commit()
        self.connection.close()

# ---------------------- HELPERS -----------------------

    def execute(self, command):
        self.connection.execute(command)
