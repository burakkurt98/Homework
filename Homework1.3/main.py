def main():
    vize1 = float(input("Vize 1 notunuzu giriniz :"))
    vize2 = float(input("Vize 2 notunuzu giriniz :"))
    final = float(input("Final notunuzu giriniz :"))
    if 101 > vize1 > 0 and 101 > vize2 > 0 and 101 > final > 0:
        toplam = (vize1 // 10) * 3 + (vize2 // 10) * 3 + (final // 10) * 4
        if toplam >= 90:
            print("AA")
        elif 90 > toplam >= 85:
            print("BA")
        elif 85 > toplam >= 80:
            print("BB")
        elif 80 > toplam >= 75:
            print("CB")
        elif 75 > toplam >= 70:
            print("CC")
        elif 70 > toplam >= 65:
            print("DC")
        elif 65 > toplam >= 60:
            print("DD")
        else:
            print("FF")


if __name__ == '__main__':
    main()
