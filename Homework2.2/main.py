class Insan():
    def __init__(self):
        self.ad = "Burak"
        self.soyad = "Kurt"
        self.yas = 23
        self.ulke = "Turkiye"
        self.sehir = "istanbul"
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenek_ekle(self, yetenekEkle):
        self.yetenekler.append(yetenekEkle)


def main():
    obje_insan = Insan()
    obje_insan.yetenek_ekle("Python")
    obje_insan.yetenek_ekle("Oyun oynamak")
    obje_insan.yetenek_ekle("Kod yazmak")
    print(obje_insan.kisi_bilgileri())


if __name__ == '__main__':
    main()
