# Akıllı Tatil Planlama ve Bütçe Kontrol Sistemi
# Kullanıcıdan tatil bilgilerini alır, maliyeti hesaplar,
# indirimleri uygular ve tatil planına puan verir.

print("Akıllı Tatil Planlama Sistemine Hoş Geldiniz")
print("-" * 45)

# --- Kullanıcı bilgilerini al ---
ad = input("Adınız: ")
yas = int(input("Yaşınız: "))
butce = float(input("Toplam bütçeniz (TL): "))
tatil_suresi = int(input("Kaç gün tatil yapacaksınız: "))
kisi_sayisi = int(input("Kaç kişi gideceksiniz: "))

sehir = input("Gitmek istediğiniz şehir (Antalya / İstanbul / Kapadokya / Trabzon): ")
hava_durumu = input("Hava durumu nasıl? güneşli / yağmurlu / karlı: ").lower()
ulasim = input("Ulaşım şekli nedir? uçak / otobüs / araba: ").lower()

# --- Tatil seçenekleri (veri yapıları) ---
sehirler = ["Antalya", "İstanbul", "Kapadokya", "Trabzon"]

# Tuple değiştirilemez, ulaşım seçenekleri sabit
ulasim_secenekleri = ("uçak", "otobüs", "araba")

# Set içinde aynı eleman iki kez bulunmaz
aktiviteler = {"müze", "doğa yürüyüşü", "yüzme"}

# Şehirlerin günlük otel ücretleri
otel_fiyatlari = {
    "Antalya": 2500,
    "İstanbul": 3000,
    "Kapadokya": 2200,
    "Trabzon": 1800
}

# Kişi başı ulaşım ücretleri
ulasim_fiyatlari = {
    "uçak": 3000,
    "otobüs": 1200,
    "araba": 1800
}

# --- Şehir kontrolü ---
if sehir not in sehirler:
    print("Bu şehir için henüz tatil planımız bulunmuyor.")
else:
    print("Şehir seçiminiz kabul edildi.")

    # --- Otel maliyeti ---
    gunluk_otel_fiyati = otel_fiyatlari[sehir]
    otel_maliyeti = gunluk_otel_fiyati * tatil_suresi
    toplam_otel_maliyeti = otel_maliyeti * kisi_sayisi

    # --- Ulaşım maliyeti ---
    if ulasim in ulasim_secenekleri:
        kisi_basi_ulasim = ulasim_fiyatlari[ulasim]
        toplam_ulasim_maliyeti = kisi_basi_ulasim * kisi_sayisi
    else:
        toplam_ulasim_maliyeti = 0
        print("Geçersiz ulaşım seçeneği girdiniz.")

    # --- Yemek maliyeti ---
    gunluk_yemek_ucreti = 750
    toplam_yemek_maliyeti = gunluk_yemek_ucreti * tatil_suresi * kisi_sayisi

    # --- Genel maliyet (indirimsiz) ---
    toplam_maliyet = (
        toplam_otel_maliyeti
        + toplam_ulasim_maliyeti
        + toplam_yemek_maliyeti
    )

    # --- Yaşa göre indirim ---
    # 0-6: %50, 7-18: %20, 19-64: yok, 65+: %30
    if yas >= 0 and yas <= 6:
        indirim_orani = 0.50
    elif yas <= 18:
        indirim_orani = 0.20
    elif yas < 65:
        indirim_orani = 0
    else:
        indirim_orani = 0.30

    indirim_miktari = toplam_maliyet * indirim_orani
    indirimli_maliyet = toplam_maliyet - indirim_miktari

    # --- Uzun tatil indirimi (7 gün ve üzeri %10) ---
    if tatil_suresi >= 7:
        uzun_tatil_indirimi = indirimli_maliyet * 0.10
        indirimli_maliyet = indirimli_maliyet - uzun_tatil_indirimi
    else:
        uzun_tatil_indirimi = 0

    # --- Grup indirimi ---
    # 1-2 kişi: yok, 3-4 kişi: %5, 5+ kişi: %10
    if kisi_sayisi >= 5:
        grup_indirimi = indirimli_maliyet * 0.10
    elif kisi_sayisi >= 3:
        grup_indirimi = indirimli_maliyet * 0.05
    else:
        grup_indirimi = 0

    indirimli_maliyet = indirimli_maliyet - grup_indirimi

    # --- Bütçe kontrolü ve yorum ---
    if butce >= indirimli_maliyet:
        kalan_para = butce - indirimli_maliyet

        print("Bütçeniz tatil için yeterli.")
        print("Tatilden sonra kalan paranız:", kalan_para, "TL")

        # İç içe koşul: kalan paraya göre yorum
        if kalan_para >= 10000:
            print("Bütçeniz oldukça rahat.")
        elif kalan_para >= 5000:
            print("Bütçeniz yeterli, ancak harcamalarınıza dikkat edin.")
        else:
            print("Tatil yapılabilir fakat çok az paranız kalacak.")
    else:
        eksik_para = indirimli_maliyet - butce

        print("Bütçeniz tatil için yeterli değil.")
        print("Eksik olan miktar:", eksik_para, "TL")

    # --- Hava durumuna göre etkinlik önerisi ---
    if hava_durumu == "güneşli":
        print("Önerilen etkinlik: Yüzme veya doğa yürüyüşü")
    elif hava_durumu == "yağmurlu":
        print("Önerilen etkinlik: Müze veya kapalı alan gezisi")
    elif hava_durumu == "karlı":
        print("Önerilen etkinlik: Kayak veya kar yürüyüşü")
    else:
        print("Hava durumu için özel bir öneri bulunamadı.")

    # --- Şehre göre özel öneri (mantıksal operatörler) ---
    if sehir == "Antalya" and hava_durumu == "güneşli":
        print("Antalya için deniz ve plaj etkinliği önerilir.")
    elif sehir == "Trabzon" and hava_durumu == "yağmurlu":
        print("Trabzon'da kapalı alanları ve müzeleri ziyaret edebilirsiniz.")
    elif sehir == "Kapadokya" and hava_durumu != "yağmurlu":
        print("Balon turu için hava koşulları uygun olabilir.")
    elif sehir == "İstanbul" and (
        hava_durumu == "güneşli" or hava_durumu == "karlı"
    ):
        print("Boğaz turu veya tarihî yarımada gezisi yapabilirsiniz.")
    else:
        print("Standart şehir turu önerilir.")

    # --- Tatil planına puan ver ---
    tatil_puani = 50

    if butce >= indirimli_maliyet:
        tatil_puani += 20
    else:
        tatil_puani -= 20

    if tatil_suresi >= 5:
        tatil_puani += 10
    else:
        tatil_puani += 5

    if hava_durumu == "güneşli":
        tatil_puani += 15
    elif hava_durumu == "yağmurlu":
        tatil_puani += 5
    else:
        tatil_puani += 10

    # --- Puan yorumu ---
    if tatil_puani >= 90:
        print("Mükemmel bir tatil planı!")
    elif tatil_puani >= 70:
        print("Oldukça iyi bir tatil planı.")
    elif tatil_puani >= 50:
        print("Ortalama bir tatil planı.")
    else:
        print("Tatil planınızı yeniden düzenlemelisiniz.")

    # --- Tatil özeti (sözlük) ---
    tatil_ozeti = {
        "ad": ad,
        "yas": yas,
        "sehir": sehir,
        "tatil_suresi": tatil_suresi,
        "kisi_sayisi": kisi_sayisi,
        "ulasim": ulasim,
        "butce": butce,
        "toplam_maliyet": indirimli_maliyet,
        "tatil_puani": tatil_puani
    }

    print("\n--- TATİL PLANI ÖZETİ ---")
    print("Müşteri:", tatil_ozeti["ad"])
    print("Şehir:", tatil_ozeti["sehir"])
    print("Tatil süresi:", tatil_ozeti["tatil_suresi"], "gün")
    print("Kişi sayısı:", tatil_ozeti["kisi_sayisi"])
    print("Ulaşım:", tatil_ozeti["ulasim"])
    print("Toplam bütçe:", tatil_ozeti["butce"], "TL")
    print("Tatil maliyeti:", tatil_ozeti["toplam_maliyet"], "TL")
    print("Tatil puanı:", tatil_ozeti["tatil_puani"])
