import sqlite3

class VendorManager:
    def __init__(self, db_manager):
        self.db = db_manager
 
    def add_vendor(self, vendor_name, country):
        query = "INSERT INTO Vendors (vendor_name, country) VALUES (?, ?)"
        self.db.cursor.execute(query, (vendor_name, country))
        self.db.connection.commit()
        print(f"Başarılı: '{vendor_name}' sisteme eklendi.")
 
    def get_all_vendors(self):
        query = "SELECT * FROM Vendors"
        self.db.cursor.execute(query)
        vendors = self.db.cursor.fetchall()

        print(f"{'ID':<5} | {'Üretici Adı':<20} | {'Ülke':<25}")
        print("-" * 55)
        for vendor in vendors:
            print(f"{vendor[0]:<5} | {vendor[1]:<20} | {vendor[2]:<25}")
 
    def delete_vendor(self, vendor_id):
        check_query = "SELECT vendor_id FROM Vendors WHERE vendor_id = ?"
        self.db.cursor.execute(check_query, (vendor_id,))
        vendor = self.db.cursor.fetchone()
        
        if vendor is None:
            print(f"{vendor_id} ID'li üretici sistemde bulunamadı!")
            return 
        
        else:
            query = "DELETE FROM Vendors WHERE vendor_id = ?"
            self.db.cursor.execute(query, (vendor_id,))
            self.db.connection.commit()
            print(f"Başarılı: {vendor_id} ID'li üretici silindi.")