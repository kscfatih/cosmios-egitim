import datetime

def yas_hesapla(dogum_tarihi):
    bugun = datetime.date.today()
    yas = bugun.year - dogum_tarihi.year - ((bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day))
    return yas

def kullanici_girdisi_al():
    while True:
        try:
            tarih_girdisi = input("Doğum tarihinizi YYYY-AA-GG formatında giriniz (örn: 1990-04-15): ")
            dogum_tarihi = datetime.datetime.strptime(tarih_girdisi, '%Y-%m-%d').date()
            return dogum_tarihi
        except ValueError:
            print("Geçersiz tarih formatı! Lütfen tekrar deneyin.")

def main():
    dogum_tarihi = kullanici_girdisi_al()
    yas = yas_hesapla(dogum_tarihi)
    print(f"Yaşınız: {yas}")

if __name__ == '__main__':
    main()