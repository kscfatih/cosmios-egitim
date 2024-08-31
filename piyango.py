import random

def kullanici_numaralari_al():
    numaralar = input("Lütfen virgülle ayrılmış 6 adet (1-49 arası) numara giriniz: ")
    numara_listesi = numaralar.split(',')
    numara_seti = {int(num) for num in numara_listesi}
    if len(numara_seti) != 6 or any(num < 1 or num > 49 for num in numara_seti):
        print("Hatalı giriş! Lütfen kurallara uygun bir giriş yapın.")
        return kullanici_numaralari_al()
    return numara_seti

def piyango_cikis_yap():
    return set(random.sample(range(1, 50), 6))

def karsilastir(kullanici_numaralari, cikan_numaralar):
    return kullanici_numaralari.intersection(cikan_numaralar)

def odul_hesapla(eslesen_sayi):
    if eslesen_sayi == 6:
        return "Büyük İkramiye!"
    elif eslesen_sayi == 5:
        return "İkinci İkramiye!"
    elif eslesen_sayi == 4:
        return "Üçüncü İkramiye"
    elif eslesen_sayi == 3:
        return "Dördüncü İkramiye"
    else:
        return "Maalesef, bu sefer kazanamadınız."

def main():
    kullanici_numaralari = kullanici_numaralari_al()
    cikan_numaralar = piyango_cikis_yap()
    eslesen_numaralar = karsilastir(kullanici_numaralari, cikan_numaralar)
    sonuc = odul_hesapla(len(eslesen_numaralar))
    
    print(f"Çekiliş sonuçları: {cikan_numaralar}")
    print(f"Sizin numaralarınız: {kullanici_numaralari}")
    print(f"Eşleşen numaralar: {eslesen_numaralar}")
    print(sonuc)

if __name__ == '__main__':
    main()