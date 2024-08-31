import datetime

def randevu_al():
    while True:
        tarih_girdisi = input("Lütfen randevu tarihinizi YYYY-AA-GG SS:DD formatında giriniz (örnek: 2023-10-01 14:30): ")
        try:
            randevu_tarihi = datetime.datetime.strptime(tarih_girdisi, "%Y-%m-%d %H:%M")
            return randevu_tarihi
        except ValueError:
            print("Geçersiz tarih formatı! Lütfen tarih ve saati doğru formatta giriniz.")

def kalan_sure_hesapla(randevu_tarihi):
    simdi = datetime.datetime.now()
    if randevu_tarihi <= simdi:
        return "Randevu tarihi geçmiş!"
    fark = randevu_tarihi - simdi
    gun = fark.days
    saat, dakika = divmod(fark.seconds, 3600)
    dakika //= 60
    return f"Randevunuza {gun} gün, {saat} saat, {dakika} dakika kaldı."

def main():
    randevu_tarihi = randevu_al()
    sonuc = kalan_sure_hesapla(randevu_tarihi)
    print(sonuc)

if __name__ == "__main__":
    main()