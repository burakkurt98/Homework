class Ogrenci():

    def __init__(self, ogrenci_adi, ogrenci_soyadı, ogrenci_no):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadı = ogrenci_soyadı
        self.ogrenci_no = ogrenci_no

    def ogrenci_bilgileri(self):
        print("Ogrenci Ad :" + self.ogrenci_adi)
        print("Ogrenci Soyad :" + self.ogrenci_soyadı)
        print("Ogrenci No :" + str(self.ogrenci_no))

class Soru():
    def net_sayisi(self, dogru_sayisi, yanlis_sayisi):
        deger = yanlis_sayisi // 4
        net = dogru_sayisi - deger
        return net
    def hesapla(self, net):
        hesap = net * 2
        return hesap

def main():
    ogrenci_ad = str(input("Ogrenci Ad :"))
    ogrenci_soyadi = str(input("Ogrenci Soyadi :"))
    ogrenci_no = int(input("Ogrenci No :"))
    dogru_sayisi = float(input("Doğru Sayisi :"))
    yanlis_sayisi = float(input("Yanlıs Sayisi :"))

    if 51 > dogru_sayisi + yanlis_sayisi:
        ogrenci_obje = Ogrenci(ogrenci_ad, ogrenci_soyadi, ogrenci_no)
        soru_objesi = Soru()
        net = soru_objesi.net_sayisi(dogru_sayisi, yanlis_sayisi)
        hesap = soru_objesi.hesapla(net)
        ogrenci_obje.ogrenci_bilgileri()
        print("Puan :", hesap)
    else:
        print("Girilen soru sayısı 50'den fazla.")

if __name__ == '__main__':
    main()
