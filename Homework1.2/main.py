birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def main():
    sayi = int(input("Bir sayi giriniz :"))
    if 9 < sayi < 100:
        def sayi_atama(sayi):
            degisken = sayi
            sayi_okusu(degisken)

        def sayi_okusu(okunucak_deger):
            birinci = okunucak_deger % 10
            ikinci = okunucak_deger // 10
            print(onlar[ikinci] + birler[birinci])

        sayi_atama(sayi)
    else:
        print("İki basamaklı bir sayı giriniz.")


if __name__ == '__main__':
    main()
