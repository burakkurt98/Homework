def bolunen_sayi_bulma(mini_sayi, max_sayi, bolunecek_sayi):
    my_list = []
    for x in range(mini_sayi, max_sayi):
        if x % bolunecek_sayi == 0:
            my_list.append(x)
    toplam_sayi = len(my_list)
    return my_list , toplam_sayi

if __name__ == '__main__':
    min_sayi = int(input("Min Sayısını Giriniz :"))
    max_sayi = int(input("Max Sayısını Giriniz :"))
    bolunecek_sayi = int(input("Bolunucek sayıyı Giriniz :"))
    print(bolunen_sayi_bulma(min_sayi, max_sayi, bolunecek_sayi))
