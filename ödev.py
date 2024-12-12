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
    print("Mach hızı, bir cismin hızının sesin hızına oranıdır.Sesin hızı belirli bir ortamda (genellikle deniz seviyesinde ve 15°C sıcaklıkta) yaklaşık 1225 km/h'dir.")
    print("Mach 0.20 - Mach 0.30: Genellikle yolcu uçakları.(yaklaşık 250km/h)")
    print("Mach 0.30 - Mach 0.50: Gösteri uçakları.(yaklaşık 300km/h)")
    print("Mach 0.50 ve üzeri: Savaş uçakları ve hipersonik uçuşlar.(yaklaşık 612km/h)")
    print("Mach 1.0: Ses hızı (yaklaşık 1225 km/h, deniz seviyesinde).")
    print("Mach 5.0: Hipersonik hız - İnsan yapımı araçlar için çok yüksek hız.")

def ucak_siniflandir(mach_hiz):
    if mach_hiz >= MACH_0_30:
        return "Savaş Uçağı"
    elif MACH_0_25 < mach_hiz < MACH_0_30:
        return "Gösteri Uçağı"
    else:
        return "Yolcu Uçağı"

def ucak_bilgisi_yazdir(isim):
    mach_hiz = ucak_verileri.get(isim)
    if mach_hiz:
        kategori = ucak_siniflandir(mach_hiz)
        print(f"\nUçak İsmi: {isim}\nMach Hızı: {mach_hiz}\nKategori: {kategori}")
    else:
        print("Bu isimde bir uçak bulunamadı.")

def ucak_secimi():
    while True:
        try:
            print("\nLütfen bir uçak seçin:")
            for i, isim in enumerate(ucak_verileri, 1):
                mach_hiz = ucak_verileri[isim]
                print(f"[{i}] {isim} - Mach {mach_hiz}")
            print("[11] Ana Menüyeye Dön")
            
            secim = input(f"Seçiminiz (1-{len(ucak_verileri)} veya 11): ").strip().lower()
            if secim == '11':
                return None  
            elif secim.isdigit() and 1 <= int(secim) <= len(ucak_verileri):
                return list(ucak_verileri)[int(secim) - 1]
            else:
                print("Geçersiz seçim, 1-10 arasında bir sayı girin.")
        except ValueError:
            print("Geçersiz giriş! Lütfen bir seçim yapın.")

def siniflandirma_ve_yazdir():
    savas_ucaklari = []
    gosteri_ucaklari = []
    yolcu_ucaklari = []

    for isim, mach_hiz in ucak_verileri.items():
        kategori = ucak_siniflandir(mach_hiz)
        if kategori == "Savaş Uçağı":
            savas_ucaklari.append((isim, mach_hiz))
        elif kategori == "Gösteri Uçağı":
            gosteri_ucaklari.append((isim, mach_hiz))
        else:
            yolcu_ucaklari.append((isim, mach_hiz))

    print("\nSavaş Uçakları:")
    for isim, mach_hiz in savas_ucaklari:
        print(f"{isim} - Mach {mach_hiz}")

    print("\nGösteri Uçakları:")
    for isim, mach_hiz in gosteri_ucaklari:
        print(f"{isim} - Mach {mach_hiz}")

    print("\nYolcu Uçakları:")
    for isim, mach_hiz in yolcu_ucaklari:
        print(f"{isim} - Mach {mach_hiz}")

def ana_menu():
    while True:
        print("\n=== Uçak Sınıflandırma Sistemi ===")
        print("[1] Uçakları Sınıflandırma")
        print("[2] Uçak Seçme ve Bilgilerini Gösterme")
        print("[3] Çıkış")

        try:
            secim = int(input("Lütfen bir seçenek seçin: "))

            if secim == 1:
                siniflandirma_ve_yazdir()
            elif secim == 2:
                secilen_ucak = ucak_secimi()
                if secilen_ucak:
                    ucak_bilgisi_yazdir(secilen_ucak)
                else:
                    continue 
            elif secim == 3:
                print("Çıkış yapılıyor...")
                quit()
                break  
            else:
                print("Geçersiz seçenek!!! Lütfen tekrar deneyin.")
        except ValueError:
            print("Geçersiz giriş!!! Lütfen İNTEGER DEĞER girin.")

if __name__ == "__main__":
    mach_aciklamalari()  
    ana_menu()  
