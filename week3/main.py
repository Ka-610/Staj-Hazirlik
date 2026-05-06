from src.db_manager import DatabaseManager
from src.app_manager import ApplicationManager
from src.vendor_manager import VendorManager

def show_menu():
 print("\n--- RAYNET CLI YÖNETİCİSİ ---")
 print("1. Uygulamaları Listele")
 print("2. Yeni Uygulama Ekle")
 print("3. Uygulama Sil")
 print("4. Üreticileri Listele")
 print("5. Yeni Üretici Ekle")
 print("6. Üretici Sil")
 print("0. Çıkış")
 return input("Seçiminiz: ")
if __name__ == "__main__":
 # Bağlantı yolunu database klasörüne yönlendiriyoruz
 db = DatabaseManager("database/raynet_manager.db")
 app_manager = ApplicationManager(db)
 vendor_manager = VendorManager(db)
 while True:
    choice = show_menu()
    if choice == '1':
        app_manager.get_all_apps()
    elif choice == '2':
        name = input("Uygulama Adı: ")
        cat = input("Kategori: ")
        vid = input("Üretici ID (Sayı): ")
        app_manager.add_app(name, cat, vid)
    elif choice == '3':
        app_id = input("Silinecek Uygulama ID: ")
        app_manager.delete_app(app_id)
    elif choice == '4':
        vendor_manager.get_all_vendors()
    elif choice == '5':
        name = input("Üretici Adı: ")
        country = input("Ülke: ")
        vendor_manager.add_vendor(name, country)
    elif choice == '6':
        vendor_id = input("Silinecek Üretici ID: ")
        vendor_manager.delete_vendor(vendor_id)
    elif choice == '0':
        print("Sistemden çıkılıyor. Auf Wiedersehen!")
        break
    else:
        print("Hatalı seçim, tekrar deneyin.")