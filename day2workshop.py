derssayisi = int(input("ders sayısı giriniz:"))

gecilen_ders = 0 

for i in range (1,derssayisi,+1):
    vize = float(input(f"vize{i}: "))
    final = float(input(f"final{i}: "))
    ortalama = (vize*0.4)+(final*0.6)

if (ortalama<49):
    harf = 'FF'
if (ortalama>=50) and (ortalama<59):
    harf = "DD"
if (ortalama>=60) and (ortalama<69):
    harf = "CC"
if (ortalama>=70) and (ortalama<79):
    harf = "BB"
if (ortalama>=80) and (ortalama<=100):
    harf = "AA"

print (f"Not ortalaması: {ortalama}, Harf notu: {harf}")

if harf != 'FF':
    gecilen_ders+=1

print (f"Geçilen ders sayısı: {gecilen_ders}")

