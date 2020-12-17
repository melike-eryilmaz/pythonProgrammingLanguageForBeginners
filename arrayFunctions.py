#17/12/2020 Array functions 

sehirler = ['Ankara','İstanbul','Mersin','Ankara']


#clear() fonksiyonu diziyi temizler.Tüm elemanları siler.
#sehirler.clear()
print(sehirler)

#count() fonksiyonu dizide o elemanın kaç kez yer aldığını verir.
print('Ankara sayısı = '+str(sehirler.count('Ankara')))

#index() fonkiyonu dizide o elemanın hangi indexte olduğunu verir ilk bulduğu indexi döner ve aramayı bırakır.
print('Ankara İndexi = '+str(sehirler.index('Ankara')))

#pop() fonksiyonu dizi içerisinden eleman silmek için kullanılır remove gibi fakat indexler ile işlem yapar.
sehirler.pop(3)
print(sehirler)


#insert() fonksiyonu dizi içerisine verilen indexe elaman eklememizi sağlar.
sehirler.insert(2,'Edirne')
print(sehirler)

#reverse() fonksiyonu diziyi ters çevirmemizi sağlar.
sehirler.reverse()
print(sehirler)

#Zaman zaman dizlerin kopyasını tutmak isteyebiliriz .Bunun için aşağıdaki gibi sehirler2 şeklinde yeni bir dizi oluşturabiliriz.
#sehirler2 dizisinde herhangi bir elemanın değerini değiştirirsek seh,rler diziside değişir .
#Bunun sebebi dizi yapılarının referams tipte olmasıdır.Yani bellekte yeri işaret ettiği için birinin değeri değiştiği zaman diğeri de değişir.
sehirler2 = sehirler

sehirler[2] = 'İzmir'
print(sehirler)
print(sehirler2)

#copy() fonksiyonu aşağıdaki gibi dizinin bir kopyasını almamızı sağlar.
#Kopya alınmış dizi üzerinde değişiklik yapınca referans dizi etkilenmez.
sehirler3 = sehirler.copy()
print(sehirler3)
sehirler3[3] = 'Muğla'

print(sehirler)
print(sehirler3)

#extend() fonksiyonu bir dizi arkasına diğer diziyi eklememizi sağlar.
sehirler.extend(sehirler3)
print(sehirler)

#sort() fonksiyonu dizileri alfabetik ise alfabetik şekilde sayısal ise sayısal olarak sıralamamızı sağlar.
sehirler.sort()
print(sehirler)

#Alfabetik olarak ters sıralamak için reverse() yapabiliriz.

sehirler.reverse()

print(sehirler)
