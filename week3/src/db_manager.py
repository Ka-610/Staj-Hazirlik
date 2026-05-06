import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        print(f"[Sistem] Veri tabanına bağlanıldı: {db_name}\n")

    def __del__(self):
        self.connection.close()