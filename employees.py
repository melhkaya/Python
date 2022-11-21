#! Şirket çalışanları verilerini tutan dosya oluşturulacak
#! Kullanıcıdan çalışan sayısı alınacak 
#! Çalışan sayısı kadar isim,soyisim,maaş bilgisi alınacak
#! Dosyadaki her satıra "Ad Soyad - Maaş" kalıbında çalışan bilgileri eklenecek.
#! Programın sonunda bu dosyadan bilgileri satır satır okuyup listeleyecek kod yazılacak. 
#! Eklenen çalışanlar mevcut çalışanları silmeyecek, üzerine yazılacak


while True:
    try:
       calisansayi = int(input("Çalışan sayısı girin:"))
    except ValueError:
        print ("Hatalı giriş yaptınız. Lütfen yeniden giriniz.")
    else:
        break


for i in range (1,calisansayi+1):
    isim = input(f"{i}. Çalışan ismi girin:")
    soyad = input(f"{i}. Çalışan soyadı girin: ")

while True: 
    try:
        maas = float(input(f"{i}. Çalışan maaşı girin:"))
    except:
        print ("Hatalı bilgi girdiniz.")
    else:
        break

file=open ("emoloyees.txt","a")
file.writelines (f"\n {isim} {soyad} - {maas}")
file.close()



