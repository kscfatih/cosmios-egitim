import random

def zar_at(atma_sayisi):
    sayac = 0
    for _ in range(atma_sayisi):
        if random.randint(1, 6) == 6:  # 6 sayısının gelmesini kontrol et
            sayac += 1
    return sayac

def olasilik_hesapla(atma_sayisi, gelen_sayi):
    olasilik = (gelen_sayi / atma_sayisi) * 100
    return olasilik

def main():
    atma_sayisi = 10000  # Zarın atılma sayısı
    gelen_alti_sayisi = zar_at(atma_sayisi)
    olasilik = olasilik_hesapla(atma_sayisi, gelen_alti_sayisi)
    print(f"{atma_sayisi} kez zar atıldığında 6 sayısı {gelen_alti_sayisi} kez geldi.")
    print(f"6 sayısının gelme olasılığı yaklaşık %{olasilik:.2f}.")

if __name__ == '__main__':
    main()

