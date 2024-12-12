import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

MACH_0_25 = 0.25
MACH_0_30 = 0.30

ucak_verileri = {
    "F-16 Falcon": 0.28,
    "F-22 Raptor": 0.35,
    "Boeing 747": 0.22,
    "Eurofighter Typhoon": 0.40,
    "Cessna 172": 0.20,
    "Su-57 Felon": 0.36,
    "Dassault Rafale": 0.33,
    "MiG-29 Fulcrum": 0.31,
    "Concorde": 0.34,
    "Airbus A380": 0.24,
}

def mach_aciklamalari():
    return (
        "Mach hızı, bir cismin hızının sesin hızına oranıdır. Sesin hızı belirli bir ortamda (genellikle deniz seviyesinde ve 15°C sıcaklıkta) yaklaşık 1225 km/h'dir.\n"
        "Mach 0.20 - Mach 0.30: Genellikle yolcu uçakları.\n"
        "Mach 0.30 - Mach 0.50: Gösteri uçakları.\n"
        "Mach 0.50 ve üzeri: Savaş uçakları ve hipersonik uçuşlar.\n"
        "Mach 1.0: Ses hızı (yaklaşık 1225 km/h, deniz seviyesinde).\n"
        "Mach 5.0: Hipersonik hız - İnsan yapımı araçlar için çok yüksek hız."
    )

def ucak_siniflandir(mach_hiz):
    if mach_hiz >= MACH_0_30:
        return "Savaş Uçağı"
    elif MACH_0_25 < mach_hiz < MACH_0_30:
        return "Gösteri Uçağı"
    else:
        return "Yolcu Uçağı"

def ucak_bilgisi_yazdir(isim):
    if isim in ucak_verileri:
        mach_hiz = ucak_verileri[isim]
        kategori = ucak_siniflandir(mach_hiz)
        return f"\nUçak İsmi: {isim}\nMach Hızı: {mach_hiz}\nKategori: {kategori}"
    else:
        return "Bu isimde bir uçak bulunamadı."

def secim_yapildi():
    secilen_ucak = ucak_secim.get()
    if secilen_ucak:
        mesaj = ucak_bilgisi_yazdir(secilen_ucak)
    else:
        mesaj = "Lütfen bir uçak seçin."
    
    bilgi_label.config(text=mesaj)

def giris_yap():
    girilen_sifre = sifre_entry.get()
    if girilen_sifre == "123":
        sifre_frame.destroy()  # Şifre penceresini kapat
        ana_menu()  # Ana menüyü aç
    else:
        messagebox.showerror("Hata", "Yanlış şifre. Lütfen tekrar deneyin.")

def sifre_girisi():
    global sifre_frame, sifre_entry
    sifre_frame = tk.Tk()
    sifre_frame.title("Giriş")
    sifre_frame.geometry("300x150")
    
    tk.Label(sifre_frame, text="Şifreyi girin:", font=("Arial", 12)).pack(pady=10)
    sifre_entry = tk.Entry(sifre_frame, show="*", font=("Arial", 14))
    sifre_entry.pack(pady=10)
    tk.Button(sifre_frame, text="Giriş", command=giris_yap, font=("Arial", 12)).pack(pady=10)

    sifre_frame.mainloop()

def ana_menu():
    uckak_listesi = list(ucak_verileri.keys())
    ana_pencere = tk.Tk()
    ana_pencere.title("Uçak Seçim Sistemi")
    ana_pencere.attributes("-fullscreen", True)
    
    image_path = r"C:\Users\hp\OneDrive\Resimler\Screenshots\k.png"
    try:
        img = Image.open(image_path)
        img = img.resize((ana_pencere.winfo_screenwidth(), ana_pencere.winfo_screenheight()))
        img = ImageTk.PhotoImage(img)
        
        background_label = tk.Label(ana_pencere, image=img)
        background_label.place(relwidth=1, relheight=1)
    except Exception as e:
        print(f"Resim yüklenemedi: {e}")

    global bilgi_label
    bilgi_label = tk.Label(ana_pencere, text="Uçak bilgilerini görmek için bir seçenek seçin.", font=("Arial", 18), fg="white", bg="black")
    bilgi_label.pack(pady=10)

    global ucak_secim
    ucak_secim = tk.StringVar()
    ucak_secim.set("Seçiminizi yapın...")  

    ucak_secim_menu = tk.OptionMenu(ana_pencere, ucak_secim, *uckak_listesi)
    ucak_secim_menu.pack(pady=10)

    secim_button = tk.Button(ana_pencere, text="Uçak Seç", command=secim_yapildi, font=("Arial", 14))
    secim_button.pack(pady=10)

    aciklama_button = tk.Button(ana_pencere, text="Mach Hızları Açıklamaları", command=lambda: messagebox.showinfo("Mach Hızları", mach_aciklamalari()), font=("Arial", 14))
    aciklama_button.pack(pady=10)

    exit_button = tk.Button(ana_pencere, text="Çıkış", command=ana_pencere.destroy, font=("Arial", 14), fg="red")  # Çıkış butonu
    exit_button.pack(pady=10)

    ana_pencere.mainloop()

if __name__ == "__main__":
    sifre_girisi()  # Şifre girme ekranını başlat

