# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:07:47 2020

@author: Melike.Eryilmaz
"""

# Eğer birden fazla oğrenciniz olan bir öğretmen olsaydınız oğrencilerinizi ayrı ayrı yerlerde tutmak yerine
#tek bir listede sıra ile tutmayı tercih ederdiniz .Dizilerde bu mantık ile çalışmaktadır.
# ogrenci1 = "Melike"
# ogrenci2 = "Leyla"
# ogrenci3 = "Adnan"
#17/12/2020

# print(ogrenci1)

# print(ogrenci2)

# print(ogrenci3)



ogrenciler = ['Melike','Leyla','Adnan']

print(ogrenciler[2]) 

#Diziye yeni bir eleman eklemek için append() fonksiyonu kullanılır.
ogrenciler.append('Merve')

print(ogrenciler)

#Diziden bir eleman silmek için remove() fonksiyonu kullanılır.

ogrenciler.remove('Leyla')

print(ogrenciler)

#Dizi oluştururma list constructor ile de yapılabilir.

sehirler = list(('New york','Los Angeles','Boston'))
print(sehirler)

print(len(sehirler))

#print(sehirler[3]) #Bu satırı açarsanız out of range hatası verir çünkü dizi 2 indexlidir şu anda.

sehirler.append('Şikago')

print(sehirler[3])# Burada ise bir üst satırda diziye yeni bir eleman eklendiği için hata vermemekte,dizinin 3. indexindeki elemanı ekranı yazdırmaktadır.
