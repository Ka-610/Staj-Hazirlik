import sqlite3

class ApplicationManager:
    def __init__(self, db_manager):
        self.db = db_manager
 # CREATE (Ekleme) - SQL Injection korumalı
    def add_app(self, app_name, category, vendor_id):
        query = "INSERT INTO Applications (app_name, category, vendor_id) VALUES (?, ?, ?)"
        self.db.cursor.execute(query, (app_name, category, vendor_id))
        self.db.connection.commit()
        print(f"Başarılı: '{app_name}' sisteme eklendi.")
 # READ (Okuma)
    def get_all_apps(self):
        query = "SELECT * FROM Applications"
        self.db.cursor.execute(query)
        apps = self.db.cursor.fetchall()

        print(f"{'ID':<5} | {'Uygulama Adı':<20} | {'Kategori':<15} | {'Üretici ID':<5}")
        print("-" * 55)
        for app in apps:
            print(f"{app[0]:<5} | {app[1]:<20} | {app[2]:<15} | {app[3]:<5}")
 # DELETE (Silme)
    def delete_app(self, app_id):
        query = "DELETE FROM Applications WHERE app_id = ?"
        self.db.cursor.execute(query, (app_id,))
        self.db.connection.commit()
        print(f"Başarılı: {app_id} ID'li uygulama silindi.")