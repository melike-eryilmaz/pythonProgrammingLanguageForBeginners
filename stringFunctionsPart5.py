#12/12/2020 split() ve strip() fonksiyonları

# split fonksiyonu boşluk karakteri default olmak üzere verilen karaktere göre  string dizi içerisindeki elemanları ayırır.
# Strip metodu, karakter dizisinin baş ve sondaki boşluk karakterlerini siler. 

info  = '  Melike Eryılmaz 23 Antalya '
info2 = ' Melike;Eryılmaz;23;İstanbul'
print(info.split())

print(info.split(' '))

print(info2.split(';'))

print(info.strip())

