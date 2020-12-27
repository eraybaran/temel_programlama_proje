# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 01:37:43 2020

@author: Eray
"""
# Kullanacağımız kütüphanleri indiriyoruz.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Kullanıcıdan alcağımız değerler ile listeler oluşturduk.
urun = []
fiyat = []
miktar = []

# Datetime modülü ile tarih ve saat değişkenini daha sonra yazdırmak üzere oluşturduk.
date_time = datetime.now()
date = datetime.strftime(date_time, "%x")
time = datetime.strftime(date_time, "%X")

# Satılan ütünlerin analiz edip bir rapor elde  etmek için rapor fonksiyonunu oluşturuyoruz.
def rapor():
    """
    urun, fiyat miktar listelerini data frame yapısına çevirir
    ardından bu oluşturulan veri setinden elde ettiği sonuçları ekrana yazdırır

    Returns
    -------
    Geriye herhangi bir değer döndürmez.

    """
    # Tarih ve saati yazdırıyoruz.
    print("\n", date, 22*" ", time)
    print(14*"-", "Satış Raporu", 14*"-")
    print("\n\t\t\tÜrün Satış Tablosu")
    # DataFrame yapısı oluşturduk.
    veri = {"Ürün" : urun,
            "Fiyat" : fiyat,
            "Satış Adedi" : miktar}
    data_frame = pd.DataFrame(veri)
    # Fiyat ve satış adedi değişkenini çarparak toplam tutar sütunu oluşturduk.
    data_frame["Toplam Tutar"] = data_frame["Fiyat"] * data_frame["Satış Adedi"]
    # Oluşturduğumuz veri setini ekrana yazdırdık.
    print(data_frame)
    # Toplam tutar ve satış adedi değerlerinin toplamını aldık.
    sum1 = data_frame["Toplam Tutar"].sum()
    sum2 = data_frame["Satış Adedi"].sum()
    # urun listesinin uzunluğunu aldık.
    uzunluk = len(urun)
     # Fiyat, toplam tutar ve satış adedi değerlerinin ortalamasını aldık.
    mean1 = data_frame["Fiyat"].mean()
    mean2 = data_frame["Toplam Tutar"].mean()
    mean3 = data_frame["Satış Adedi"].mean()
    # Sütunların toplam ve ortalama değerlerini yazdırdık.
    print("\nOrtalama Değerler\nÜrünlerin Ortalama Fiyatı:", mean1, " ₺")
    print("Ortalama Toplam Tutar    :", mean2, "₺")
    print("Ortalama Satış Adedi     :", mean3, "")
    print("\nToplam Ciro                :", sum1, "₺")
    print("Toplam Satılan Ürün Sayısı :", sum2, "Adet")
    print("Satışı Yapılan Ürün Sayısı :", uzunluk, "Adet")
    # Satış adedlerinin maksimum ve minimum değerlerini aldık.
    max_satis = data_frame.sort_values(by="Satış Adedi", ascending=False)
    say1 = max_satis.iloc[0, 0]
    say2 = max_satis.iloc[0, 2]
    min_satis = data_frame.sort_values(by="Satış Adedi")
    say3 = min_satis.iloc[0, 0]
    say4 = min_satis.iloc[0, 2]
    # Satış adedlerinin maksimum ve minimum değerlerini yazdırdık.
    print("\nEn çok Satılan Ürün        :", say1, "\nSatış Sayısı\t\t       :", say2, "Adet")
    print("En Az Satılan Ürün         :", say3, "\nSatış Sayısı\t\t       :", say4, "Adet")
    # Toplam tutarların maksimum ve minimum değerlerini aldık.
    max_kazanc = data_frame.sort_values(by="Toplam Tutar", ascending=False)
    max1 = max_kazanc.iloc[0, 0]
    max2 = max_kazanc.iloc[0, 3]
    min_kazanc = data_frame.sort_values(by="Toplam Tutar")
    max3 = min_kazanc.iloc[0, 0]
    max4 = min_kazanc.iloc[0, 3]
    # Toplam tutarların maksimum ve minimum değerlerini yazdırdık.
    print("\nEn çok Ciro Yapan Ürün     :", max1, "\nToplam\t\t               :", max2, "₺")
    print("En Az Ciro Yapan Ürün      :", max3, "\nToplam\t\t               :", max4, "₺")
    # Fiyatların n maksimum ve minimum değerlerini aldık.
    max_fiyat = data_frame.sort_values(by="Fiyat", ascending=False)
    fyt1 = max_fiyat.iloc[0, 0]
    fyt2 = max_fiyat.iloc[0, 1]
    min_fiyat = data_frame.sort_values(by="Fiyat")
    fyt3 = min_fiyat.iloc[0, 0]
    fyt4 = min_fiyat.iloc[0, 1]
    # Fiyatların n maksimum ve minimum değerlerini yazdırdık.
    print("\nEn Pahalı Ürün             :", fyt1, "\nÜcreti\t\t               :", fyt2, "₺")
    print("En Ucuz Ürün               :", fyt3, "\nÜcreti                     :", fyt4, "₺")
    print(42*"-")

def grafik_satis():
    """
    Seaborn ve matplotlib kütüphanesi ile ürün
    satışlarının barplot grafiğini oluşturur.

    Returns
    -------
    Geriye herhangi bir değer döndürmez.

    """
    # DataFrame yapısını oluşturduk.
    veri = {"Ürün" : urun,
            "Fiyat" : fiyat,
            "Satış Adedi" : miktar}
    data_frame = pd.DataFrame(veri)
    # Barplot grafiği oluşturduk.
    sns.barplot(x="Ürün", y="Satış Adedi", data=data_frame)
    plt.xlabel("Ürünler", fontsize=10)
    plt.ylabel("Satılan Ürün Sayısı", fontsize=10)
    plt.title("Toplam Satışlar", fontsize=12)
    plt.show()

def grafik_fiyat():
    """
    Seaborn ve matplotlib kütüphanesi ile ürün
    fiyatlarının barplot grafiğini oluşturur.

    Returns
    -------
    Geriye herhangi bir değer döndürmez.

    """
    # DataFrame yapısını oluşturduk.
    veri = {"Ürün" : urun,
            "Fiyat" : fiyat,
            "Satış Adedi" : miktar}
    data_frame = pd.DataFrame(veri)
    # Barplot grafiği oluşturduk.
    sns.barplot(x="Ürün", y="Fiyat", data=data_frame)
    plt.xlabel("Ürün", fontsize=10)
    plt.ylabel("Fiyat", fontsize=10)
    plt.title("Ürün Fiyatları", fontsize=12)
    plt.show()

def grafik_tfiyat():
    """
    Seaborn ve matplotlib kütüphanesi ile ürünlerin toplam kazançlarının
    barplot grafiğini oluşturur.

    Returns
    -------
    Geriye herhangi bir değer döndürmez.

    """
    # DataFrame yapısını oluşturduk.
    veri = {"Ürün" : urun,
            "Fiyat" : fiyat,
            "Satış Adedi" : miktar}
    data_frame = pd.DataFrame(veri)
    data_frame["Toplam Tutar"] = data_frame["Fiyat"] * data_frame["Satış Adedi"]
    # Barplot grafiği oluşturduk.
    sns.barplot(x="Ürün", y="Toplam Tutar", data=data_frame)
    plt.xlabel("Ürün", fontsize=10)
    plt.ylabel("Fiyat", fontsize=10)
    plt.title("Ürünlerin Toplam Kazanç Miktarları", fontsize=12)
    plt.show()

def pasta_satis():
    """
    Matplotlib kütüphanesi ile ürün satışlarının
    pasta grafiğini oluşturur.

    Returns
    -------
    Geriye herhangi bir değer döndürmez.

    """
    # DataFrame yapısını oluşturduk.
    data_frame = pd.DataFrame({"Ürünler": urun,
                               "Fiyat": fiyat,
                               "Satış Adedi": miktar})
    # Fiyat ve satış adedi değişkenini çarparak toplam tutar sütunu oluşturduk.
    data_frame["Toplam Tutar"] = data_frame["Fiyat"] * data_frame["Satış Adedi"]
    # Pasta grafiği oluşturduk.
    data_frame["Satış Adedi"].plot.pie(figsize=(8, 8), autopct='%1.1f%%', shadow=True, labels=urun)
    plt.title("Satışlar Oranları", fontsize=18)
    plt.legend(loc="best")
    plt.ylabel(" ")
    plt.show()

def pasta_tfiyat():
    """
    Matplotlib kütüphanesi ile ürünlerin toplam kazançlarının
    pasta grafiğini oluşturur.

    Returns
    -------
    Geriye herhangi bir değer döndürmez.

    """
    # DataFrame yapısını oluşturduk.
    data_frame = pd.DataFrame({"Ürünler": urun,
                               "Fiyat": fiyat,
                               "Satış Adedi": miktar})
    # Fiyat ve satış adedi değişkenini çarparak toplam tutar sütunu oluşturduk.
    data_frame["Toplam Tutar"] = data_frame["Fiyat"] * data_frame["Satış Adedi"]
    # Pasta grafiği oluşturduk
    data_frame["Toplam Tutar"].plot.pie(figsize=(8, 8), autopct='%1.1f%%', shadow=True, labels=urun)
    plt.title("Toplam Kazanç Oranları", fontsize=18)
    plt.legend(loc="best")
    plt.ylabel(" ")
    plt.show()

def menu():
    """
    Kullanıcını hangi işlemi yapabileceği işlemleri
    gösteren menü oluşturur.

    Returns
    -------
    Geriye herhangi bir değer döndürmez.

    """
    print("""
 {}                 {}
|===========HOŞGELDİNİZ===========|
|                                 |
|--------------MENÜ---------------|
|                                 |
|     1)   Ürün Ekle              |
|     2)   Günlük Rapor           |
|     3)   Ürün Listesi           |
|     4)   Fiyat Listesi          |
|     5)   Satış Sayıları         |
|     6)   Satış Grafiği          |
|     7)   Fiyat Grafiği          |
|     8)   Toplam Kazanç Grafiği  |
|                                 |
|---------------------------------|
|      Programı Kapatmak İçin     |
|             0 veya 9            |
|=================================|""".format(date, time))

# Kullanıcıdan seçim yapmasını istediğimiz bir döngü oluşturduk.
while True:
    menu()  # Menu fonksiyonunu çağırıyoruz.
    secim = int(input("Tercihinizi Giriniz:"))
    # Kullanıcıdan sayılar isteyerek seçim yaptırdık.
    if secim == 1:
        # Kullanıcıdan bilgi girişi alıyoruz.
        print("\nÜrün Bilgilerini Giriniz.")
        ad = input("Adı:")
        adet = int(input("Satış Miktarı:"))
        para = float(input("Fiyat:"))
        # Aldığımız bilgileri listelere ekliyoruz.
        urun += [ad]
        fiyat += [para]
        miktar += [adet]
    elif secim == 2:    # Satş raporunu getirir.
        rapor()         # Rapor fonksiyonunu çağırdık.
    elif secim == 3:    # Ürün listesini getirir.
        data = {"Ürünler" : urun}
        liste = pd.DataFrame(data)
        SAY = len(urun)
        print("\nToplam Ürün Sayısı :", SAY, "\n\nSatılan Ürünler Aşağıdadır.")
        print(liste)
    elif secim == 4:    # Ürünlerin fiyatlarını yazdırır.
        df = pd.DataFrame({"Fiyat": fiyat}, index=urun) # Ürün fiyatlarını atadık.
        print("\nÜrün Fiyat Listesi;")
        print(df["Fiyat"])
    elif secim == 5:     # Ürünlerin satış sayılarını yazdırır.
        df2 = pd.DataFrame({"Satış Adedi": miktar}, index=urun)
        print("\nÜrün Satış Sayıları")
        print(df2["Satış Adedi"])
    elif secim == 6:     # Satış grafiğini getirir.
        grafik_satis()   # Grafik fonksiyonlarını çağırdık.
        pasta_satis()
    elif secim == 7:     # Fiyat grafiğini getirir.
        grafik_fiyat()   # Fiyat grafik fonksiyonunu çağırdık.
    elif secim == 8:     # Toplam fiyat grafiklerini getirir.
        grafik_tfiyat()  # Grafik fonksiyonlarını çağırdık.
        pasta_tfiyat()
    else:                # Programı sonlandırır.
        print('İsteğiniz üzere program sonlandırılıyor...')
        break
