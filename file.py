file = open("sample.txt", "r")
#w for write = sıfırdan yazma ("sample.txt", "w")
#a for append = üzerine ekleme ("sample.txt", "a")
# r - read ("sample.txt", "r")


file.write("hello world mm")

print(file.read())

file.close