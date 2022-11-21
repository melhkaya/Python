

#exception
try:
    examNote = float(input("Sınav notunuzu giriniz:"))
    print(examNote)
except ValueError:
    print ("Deneme123")
except ZeroDivisionError:
    print("Hiç bir sayı sıfıra bölünemez..")
except:
    print ("Doğru bir girdi girmediniz")
finally:
    print("Try except butonu sona erdi")

print("Bitti")



