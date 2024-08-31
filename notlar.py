# Öğrencilerin bilgilerini ve notlarını tutacak listeler
ogrenci_notlari = []

def harf_notu_hesapla(not_degeri):
    if not_degeri >= 90:
        return 'A'
    elif not_degeri >= 80:
        return 'B'
    elif not_degeri >= 70:
        return 'C'
    elif not_degeri >= 60:
        return 'D'
    else:
        return 'F'

def yeni_not_sorgula():
    ad = input("Öğrencinin adını giriniz: ")
    not_degeri = int(input("Öğrencinin notunu giriniz: "))
    harf_notu = harf_notu_hesapla(not_degeri)
    ogrenci_notlari.append((ad, not_degeri, harf_notu))
    print(f"{ad} öğrencisinin notu: {not_degeri}, Harf notu: {harf_notu}")

def onceki_sorgulari_goruntule():
    if len(ogrenci_notlari) == 0:
        print("Henüz herhangi bir sorgu yapılmamış.")
        return
    
    while True:
        print("\n--- Önceki Sorgular ---")
        print("1. Tüm sorguları görüntüle")
        print("2. Öğrenci adına göre arama yap")
        print("3. Geri dön")
        secim = input("Seçiminizi yapın: ")
        
        if secim == '1':
            for sorgu in ogrenci_notlari:
                print(f"Öğrenci: {sorgu[0]}, Not: {sorgu[1]}, Harf Notu: {sorgu[2]}")
        
        elif secim == '2':
            arama = input("Aramak istediğiniz öğrencinin adını girin: ")
            bulunan_sorgular = [s for s in ogrenci_notlari if arama.lower() in s[0].lower()]
            if not bulunan_sorgular:
                print("Bu isimle eşleşen öğrenci bulunamadı.")
            else:
                for sorgu in bulunan_sorgular:
                    print(f"Öğrenci: {sorgu[0]}, Not: {sorgu[1]}, Harf Notu: {sorgu[2]}")
        
        elif secim == '3':
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

def ana_menu():
    while True:
        print("\n--- Ana Menü ---")
        print("1. Yeni not sorgula")
        print("2. Önceki sorguları görüntüle")
        print("3. Programdan çık")
        secim = input("Seçiminizi yapın: ")

        if secim == '1':
            yeni_not_sorgula()
        elif secim == '2':
            onceki_sorgulari_goruntule()
        elif secim == '3':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

# Programı başlat
ana_menu()