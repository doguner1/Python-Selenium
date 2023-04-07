# Öğrenci kayıt sistemi
ogrenciler = []

# Aldığı isim soy isim ile listeye öğrenci ekleme
def ogrenci_ekle(isim, soyisim):
    ogrenci = {'isim': isim, 'soyisim': soyisim}
    ogrenciler.append(ogrenci)
    print(f"{isim} {soyisim} öğrenci listesine eklendi.")

# Aldığı isim soy isim ile eşleşen değeri listeden kaldırma
def ogrenci_sil(isim, soyisim):
    for ogrenci in ogrenciler:
        if ogrenci['isim'] == isim and ogrenci['soyisim'] == soyisim:
            ogrenciler.remove(ogrenci)
            print(f"{isim} {soyisim} öğrenci listesinden silindi.")
            return
    print(f"{isim} {soyisim} öğrenci listesinde bulunamadı.")

# Birden fazla öğrenci eklemeyi mümkün kılan
def ogrencileri_ekle():
    while True:
        isim = input("Öğrencinin adını girin (Çıkmak için q): ")
        if isim == 'q':
            break
        soyisim = input("Öğrencinin soyadını girin: ")
        ogrenci_ekle(isim, soyisim)

# Listedeki tüm öğrencileri tek tek ekrana yazdırma
def ogrencileri_listele():
    for i, ogrenci in enumerate(ogrenciler):
        print(f"{i+1}. {ogrenci['isim']} {ogrenci['soyisim']}")

# Öğrencinin numarasını öğrenmeyi mümkün kılan
def ogrenci_numarasi(ogrenci):
    for i, kayitli_ogrenci in enumerate(ogrenciler):
        if kayitli_ogrenci == ogrenci:
            return i+1
    return -1

# Birden fazla öğrenci silmeyi mümkün kılan (döngü kullanarak)
def ogrencileri_sil():
    while True:
        isim = input("Silmek istediğiniz öğrencinin adını girin (Çıkmak için q): ")
        if isim == 'q':
            break
        soyisim = input("Silmek istediğiniz öğrencinin soyadını girin: ")
        for ogrenci in ogrenciler:
            if ogrenci['isim'] == isim and ogrenci['soyisim'] == soyisim:
                ogrenciler.remove(ogrenci)
                print(f"{isim} {soyisim} öğrenci listesinden silindi.")
                break
        else:
            print(f"{isim} {soyisim} öğrenci listesinde bulunamadı.")

# Test kodu
ogrenci_ekle('Ali', 'Yılmaz')
ogrenci_ekle('Ayşe', 'Kara')
ogrenci_ekle('Mehmet', 'Demir')
ogrenci_ekle('Zeynep', 'Aydın')
ogrencileri_listele()

ogrenci_numarasi('Ayşe', 'Kara')
ogrenci_sil(2)
ogrencileri_listele()

ogrencileri_sil()
