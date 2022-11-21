#karar blokları ve döngüler 
#kullanıcıdan girdi almak 


print ('2. gün başlangıç')


#kullanıcıdan girdi almak
input()
userinput = input()
print(f'Girilen değer: (user input)')

#! type conversion
numberStr = '10'
print (type(numberStr))
number =int(numberStr)
print(number +10)
print(type(number))

userinput= input()
dersnotu = int(userinput)
print(f'ders notunuz: {dersnotu}')



#!karar yapıları


#
vize = float(input('vize: '))
final = float(input('final '))

ortalama = vize*0.4 + final*0.6

if (ortalama>=0) and (ortalama<=49):
   harf = 'FF'

elif (ortalama>50) and (ortalama<=59):
    harf = 'DD'

elif (ortalama>=60)and (ortalama<=69):
    harf = 'CC'

elif (ortalama>=70) and (ortalama<=79):
    harf = 'BB'

elif (ortalama>=80) and (ortalama<=100):
    harf = 'AA'

print (f"Not ortalaması: {ortalama}, Harf notu: {harf} ")




vizesayısı = int(input("vize sayısı giriniz: "))
