birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

def main():
    sayi = int(input("Bir sayi giriniz :"))
    if sayi > 9 and sayi < 100:
        def sayiAtama(sayi):
            degisken = sayi
            sayi_okusu(degisken)
        def sayi_okusu(okunucak_deger):
            birinci = okunucak_deger % 10
            ikinci = okunucak_deger // 10
            print(onlar[ikinci] + birler[birinci])
        sayiAtama(sayi)
    else:
        print("İki basamaklı bir sayı giriniz.")

if __name__ == '__main__':
    main()